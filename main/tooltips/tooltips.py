"""
class module to generate custom Bokeh html tooltips.
uses the HoverTool model.
"""
from bokeh.models import HoverTool

class Tooltips:
	"""
	Tooltips class.
	You can define several methods for different tooltip displays
	"""
	def profile_2d(self):
		"""
		2D profile html tooltips.
		Input is a Bokeh ColumnDataSource(cds) in order to display the column data when hovering over points.
		The columns of the dataframe are UTC and Altitude.
		The custom html is passed to hovertool as an argument.
		Returns an object that displays are datetime and altitude in customized html format.
		You can add as many details as needed.
		You can also use custom css classes.
		"""
		# DECLARE WHICH TOOLTIPS TO SHOW
		# use the required datetime format found in
		# https://docs.bokeh.org/en/latest/docs/reference/models/formatters.html
		# the UTC field is the name of the datetime column
		html_TOOLTIPS = """
		<div class='flight-profile-wrapper'>
			<div class='subwrapper-datetime'>
				<p>DateTime(UTC):@UTC{%F %H:%M}</p>
			</div>
			<div class='subwrapper-altitude'>
				<p>Altitude(ft): @Altitude</p>
			</div>
		</div>
		"""
		# PASS THE TOOLTIPS TO THE HoverTool model and Retrun
		# For datetime object use the formatter to display in human-readable form
		hover_tool = HoverTool(
			tooltips=html_TOOLTIPS,
			formatters={
				'@UTC': 'datetime',
			},
			mode='vline'
		)
		return hover_tool

def main():
    pass


if __name__ == "__main__":
	main()
