import plotly.figure_factory as ff

df = [dict(Task='Job A', Start = '2009-01-01', Finish = '2009-02-28', Complete=10),
dict(Task='Job B', Start = '2008-12-05', Finish = '2009-04-15', Complete=60),
dict(Task='Job c', Start = '2009-02-20', Finish = '2009-05-30', Complete=95)]

fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
fig.show()