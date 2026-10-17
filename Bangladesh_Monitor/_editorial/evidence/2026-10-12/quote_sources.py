import subprocess

script = "/opt/data/skills/research/grounded-citations/scripts/sources.py"
ledger = "/opt/data/obsidian-vault/Bangladesh_Monitor/_editorial/citations/2026-10-12-ledger.json"
evidence = "/opt/data/obsidian-vault/Bangladesh_Monitor/_editorial/evidence/2026-10-12/extracted-snippets.txt"
quotes = {
    1: "চট্টগ্রাম বন্দর কর্তৃপক্ষের ১ হাজার ২০০ কোটি টাকার বেশি স্থায়ী আমানত হিসেবে রাখা আছে তারল্যসংকটে থাকা ছয়টি ব্যাংকে। আমানতের অর্থ ফেরত পাওয়া নিয়ে ঝুঁকি থাকলেও বন্দর কর্তৃপক্ষ আন্তর্জাতিক মানদণ্ড অনুযায়ী সম্ভাব্য ক্ষতির জন্য হিসাবভিত্তিক কোনো সংস্থান রাখেনি।",
    2: "The parliamentary committee on government undertakings today (12 October) suggested for greater transparency and accountability in the financial management and operations of the country's three major seaports, with a focus on resolving longstanding audit objections and preventing misuse of public funds.",
    3: "Of the total expenditure, Tk 6,500 crore was spent on capital and maintenance dredging of the channel, with Tk 5,100 crore of that amount drawn directly from Bangladesh Bank’s foreign exchange reserves.",
    4: "The price of a 12kg liquefied petroleum gas (LPG) cylinder has been increased by Tk252, taking the price to Tk1,837.",
    5: "On Wednesday, a resident of Paikpara in Mirpur said a retailer demanded Tk 2,400 for a cylinder, claiming his purchase cost was Tk 2,300.",
    6: "Liquefied petroleum gas (LPG) distributors have announced a two-day nationwide shutdown of LPG shops from Thursday, demanding higher distributors' commissions, an end to alleged harassment by law enforcement agencies, and the revival of idle cylinders.",
    7: "In the first week of this month, the Bangladesh Energy Regulatory Commission (BERC) raised the official price of a 12kg cylinder by Tk 252, from Tk 1,585 to Tk 1,837. But consumers in major cities are paying up to Tk 2,500 a cylinder, well above the government rate.",
    8: "According to a study unveiled yesterday, 79 percent of the poorest families spend over 40 percent of their income repaying instalments on loans from microfinance institutions and local mohajons, or informal lenders.",
    9: "The findings were presented on Monday at a workshop in Dhaka. BIDS researcher Kazi Iqbal conducted the study, drawing mainly on data from 2012 to 2022.",
    10: "The government has set a target to collect data from an estimated 4.45 crore families and add them to a database by December, as nationwide data collection under the Family Card programme began today.",
    11: "The Family Card is a database-driven digital identification and social protection instrument designed to deliver regular financial assistance directly to vulnerable households.",
    12: "The government aims to bring 1.61 crore families under the Family Card scheme by 2030 and will distribute 41 lakh new cards nationwide in the current 2026-27 fiscal year, said State Minister for Social Welfare Farzana Sharmin Putul today (14 July).",
    13: "The collected data will be screened by AI-powered auditing software to flag discrepancies between reported income and living conditions. Supervisory teams will then recheck 5-10 percent of surveyed households to verify the information.",
    14: "Around 300 children are currently living with their incarcerated mothers in prisons across the country, prompting the Department of Social Services to recommend alternative family-based care or placement in government children’s homes to ensure their safety and development.",
    15: "দেশের বিভিন্ন কারাগারে বন্দী মায়েদের সঙ্গে প্রায় ২৯৮ থেকে ৩০৩ শিশু অবস্থান করছে।",
    16: "Data from the Department of Prisons shows that 299 children were staying with their mothers in 74 central and district jails across the country as of 26 April 2026.",
}
for source_id, text in quotes.items():
    subprocess.run(["python", script, "--ledger", ledger, "quote", str(source_id), "--text", text, "--from", evidence], check=True)
print(f"attached_quotes={len(quotes)}")
