
def clean_aircraft_subset(df_subset):
    df = df_subset.copy()
    
    df['Event.Date'] = pd.to_datetime(df['Event.Date'], errors='coerce')
    df = df[df['Event.Date'].notnull()]
    
    num_cols = [
        'Total.Fatal.Injuries', 'Total.Serious.Injuries',
        'Total.Minor.Injuries', 'Total.Uninjured',
        'Number.of.Engines'
    ]
    df[num_cols] = df[num_cols].fillna(0)

    cat_cols = [
        'Make', 'Model', 'Aircraft.Category', 'Engine.Type',
        'Amateur.Built', 'Purpose.of.flight',
        'Weather.Condition', 'Broad.phase.of.flight',
        'Injury.Severity', 'Aircraft.damage'
    ]
    df[cat_cols] = df[cat_cols].fillna("UNKNOWN")

    return df