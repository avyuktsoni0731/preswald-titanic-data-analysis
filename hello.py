from preswald import connect, get_df, query, table, text, image, sidebar, separator, slider, plotly
import plotly.express as px

# initialize connection to preswald.toml data sources
connect()
df = get_df("titanic_csv")          # loading dataset (created an import in preswald.toml)

sidebar()

image(src="https://user-images.githubusercontent.com/74038190/225813708-98b745f2-7d22-48cf-9150-083f1b00d6c9.gif")
text("# Avyukt's Data Analysis App")
separator()

# data manipulation using sql query
sql = "SELECT * FROM titanic_csv WHERE Age > 35"
filtered_df = query(sql, "titanic_csv")

text("## Filtered Data Table (Age > 35)")
table(filtered_df, title="Filtered Data")
separator()

text("## Slider Filter Table (Age)")
threshold = slider("Age", min_val=0, max_val=100, default=25)
table(df[df["Age"] > threshold], title="Age Filter Table")
separator()

# age distribution histogram
text("## Age Distribution Histogram")
fig = px.histogram(df, x="Age", title="Age Distribution")
fig.update_layout(bargap=0.2)  # Gap between bars (0 to 1)
plotly(fig)
separator()

# age vs fare scatter-plot
text("## Age vs Fare Scatter Plot")
fig2 = px.scatter(df, x="Age", y="Fare", color=df["Survived"].map({1: "Survived", 0: "Did not survive"}), hover_data=["Name", "Sex", "Pclass"], title="Age vs Fare (Colored by Survival)")
plotly(fig2)
separator()

# sex vs age (survived) violin chart
text("## Sex vs Age (Survived) Violin Chart")
fig3 = px.violin(df, y="Age", x="Sex", color="Survived", box=True, points="all")
plotly(fig3)
separator()

# survived by class pie chart distribution
survived_by_class = df[df['Survived'] == 1]['Pclass'].value_counts().reset_index()
survived_by_class.columns = ['Pclass', 'Count']

text("## Survived by Class (Pie Chart Distribution)")
fig4 = px.pie(survived_by_class, names='Pclass', values='Count', title='Survivors by Passenger Class')
plotly(fig4)
separator()










