import os
from psnawp_api import PSNAWP
from psnawp_api.models.trophies.trophy_titles import TrophyTitle
from psnawp_api.models.trophies.trophy_constants import TrophySet, PlatformType
import pandas as pd

# Get common PlatformType str
def transform_platform(platform: PlatformType) -> list[str]:
    return list(platform)[0].value

# Transform TrophySet to dict of {"tier": ammount}
def transform_trophy_set(trophy_set: TrophySet) -> dict[str: any]:
    trophy_types = [a for a in dir(trophy_set) if not a.startswith('__')]
    return {trophy_type: getattr(trophy_set, trophy_type) for trophy_type in trophy_types}

# Extract
def trophies_extract(npsso: str = os.environ.get("NPSSO"), limit: int = None) -> list[TrophyTitle]:
    psnawp = PSNAWP(npsso_cookie=npsso)
    client = psnawp.me()
    print(client.trophy_summary())
    return  [trophy_title for trophy_title in client.trophy_titles(limit=limit)]

# Optional raw export of extract result into CSV
def raw_export_to_csv(trophies_list: list[TrophyTitle], csv_path: str = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "csv_extractions", "trophies.csv")):
    raw_titles = []
    for title in trophies_list:
        title_attrs = [a for a in dir(title) if not a.startswith('__')]
        raw_titles.append({attr: getattr(title, attr) for attr in title_attrs})
    df = pd.DataFrame(raw_titles)
    df.to_csv(csv_path)

# Transform the Extract Output
def trophies_transform(trophies_list: list[TrophyTitle]):
    data = []
    # Generate one row for each title with wanted raw data
    for title in trophies_list:
        title_data = {
            "game_id": title.np_communication_id,
            "name": title.title_name,
            "platform": title.title_platform,
            "progress": title.progress,
            "earned": title.earned_trophies,
            "total": title.defined_trophies,
            "last_played": title.last_updated_date_time,
            "trophies_version": title.trophy_set_version,
            "game_icon_url": title.title_icon_url,
            "has_extra_trophies": title.has_trophy_groups,
        }
        data.append(title_data)
    # Create Dataframe from raw data
    df = pd.DataFrame(data=data)
    # Transform all platforms and trophy sets
    df["platform"] = df["platform"].map(transform_platform)
    df["earned"] = df["earned"].map(transform_trophy_set)
    df["total"] = df["total"].map(transform_trophy_set)
    # Split trophy sets into separate columns
    split_earned_df = pd.json_normalize(df["earned"]).add_prefix("earned_")
    split_total_df = pd.json_normalize(df["total"]).add_prefix("total_")
    # Concatenate all dataframes and drop the original trophy set columns
    df = pd.concat([df, split_earned_df, split_total_df], axis=1)
    df.drop(["earned", "total"], axis=1, inplace=True)
    return df

if __name__ == "__main__":
    trophies_list = trophies_extract()
    df = trophies_transform(trophies_list=trophies_list)
    print(df)