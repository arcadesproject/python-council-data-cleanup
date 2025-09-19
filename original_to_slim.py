"""
Trims the data into spending
by category for easily comparisons
"""
import pandas as pd

# Load full dataset
df = pd.read_csv("Revenue_Outturn_time_series_data_v2.3.csv")

# Columns we want
cols_to_keep = [
    "year_ending", "ONS_code", "LA_name",
    "RS_edu_net_exp",    # Education
    "RS_trans_net_exp",  # Highways & Transport
    "RS_csc_net_exp",    # Children Social Care
    "RS_asc_net_exp",    # Adult Social Care
    "RS_phs_net_exp",    # Public Health
    "RS_hous_net_exp",   # Housing
    "RS_cul_net_exp",    # Culture
    "RS_env_net_exp",    # Environment
    "RS_plan_net_exp",   # Planning
    "RS_pol_net_exp",    # Police
    "RS_frs_net_exp",    # Fire & Rescue
    "RS_cen_net_exp",    # Central Services
    "RS_oth_net_exp",    # Other
    "RS_totsx_net_exp"   # Total
]

slim = df[cols_to_keep]

# Friendlier names for frontend
rename_map = {
    "RS_edu_net_exp": "Education",
    "RS_trans_net_exp": "Highways_Transport",
    "RS_csc_net_exp": "Children_Social_Care",
    "RS_asc_net_exp": "Adult_Social_Care",
    "RS_phs_net_exp": "Public_Health",
    "RS_hous_net_exp": "Housing",
    "RS_cul_net_exp": "Culture",
    "RS_env_net_exp": "Environment",
    "RS_plan_net_exp": "Planning",
    "RS_pol_net_exp": "Police",
    "RS_frs_net_exp": "Fire_Rescue",
    "RS_cen_net_exp": "Central_Services",
    "RS_oth_net_exp": "Other",
    "RS_totsx_net_exp": "Total"
}
slim = slim.rename(columns=rename_map)

# Save both CSV and JSON (pick whichever works best on frontend)
slim.to_csv("slim_spending.csv", index=False)
slim.to_json("slim_spending.json", orient="records", indent=4)

# Group by 'year_ending' and sum the expenditure values
yearly_totals = slim.groupby("year_ending").sum()
# Save the summary table as a CSV (for future reference)
yearly_totals.to_csv("yearly_expenditure_totals.csv", index=False)
# Save as JSON
yearly_totals.to_json("yearly_expenditure_totals.json", orient="records", indent=4)
