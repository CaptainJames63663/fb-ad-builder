import pandas as pd
import streamlit as st

st.title("📦 Cap's Facebook Ad Template Builder")

uploaded_file = st.file_uploader("Upload your sniper sheet (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    ads = []

    for _, row in df.iterrows():
        title = row["Title"]
        est_value = row["Estimated Value"]
        bid = row["Current Bid"]
        profit = row["Estimated Flip $"]
        time_to_flip = row["Time to Flip"]

        if est_value <= 0 or bid <= 0:
            continue

        margin = profit / bid if bid else 0
        list_price = round(est_value * 0.8) if margin >= 2 else est_value

        desc = f"""For Sale: {title}

Professionally maintained or lightly used — a solid piece with plenty of value left. Ideal for resale, use, or as a long-term asset.

Estimated resale value: ${est_value:,}
Asking just: ${list_price:,}

⏱️ Fast flips in {time_to_flip} — priced to move.
📍 Local pickup only (37037) — I’ll help load if it’s a big item.

Cross-posted. First come, first served."""

        ads.append({"Title": title, "Listing Price": list_price, "Ad Description": desc})

    ad_df = pd.DataFrame(ads)
    st.success("Generated ad templates!")
    st.dataframe(ad_df)

    csv = ad_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Ad Templates CSV",
        data=csv,
        file_name="fb_marketplace_ads.csv",
        mime="text/csv"
    )
