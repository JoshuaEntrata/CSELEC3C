%pip install plotly

------------next cell---------------
import plotly.graph_objects as go

# Filter the merged_df to only include rows where item_code = 2805 &  element_code = 5142)
filtered_df_2805 = merged_df[(merged_df['item_code'] == 2805) & (merged_df['element_code'] == 5142)]

# Select the required columns
df_map = filtered_df_2805[['area_abbreviation', 'item_code', 'y2000']]

------------next cell---------------

df_aggregated = df_map.groupby('area_abbreviation', as_index=False).agg({'y2000': 'sum'})

# Create a Choropleth map
fig = go.Figure(data=go.Choropleth(
    locations=df_aggregated['area_abbreviation'],  # ISO Alpha-3 country codes
    z=df_aggregated['y2000'],            # Data values
    colorscale='Viridis',         # Color scale
    colorbar=dict(
        title="2010 Value",       # Title for the color bar
        thickness=15,             # Thickness of the color bar
    ),
    marker_line_color='darkgray',  # Country borders color
    marker_line_width=0.5         # Country borders width
))

# Update the layout for the map
fig.update_layout(
    geo=dict(
        showframe=False,          # Hide the frame around the map
        showcoastlines=False,     # Hide coastlines
        projection_type='equirectangular'  # Type of map projection
    ),
    margin={"r":0,"t":0,"l":0,"b":0} ,# Remove margins
     title={
        'text': "Choropleth Map of 2000 [Rice (Milled Equivalent) : Food]",  # Main title
        'x': 0.5,                                # Title position (x-center)
        'xanchor': 'center',                    # Center the title
        'y': 0.2,                              # Title position (y-top)
        'yanchor': 'top'                        # Anchor the title to the top
    },
)
# Show the plot
fig.show()

