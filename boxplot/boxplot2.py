from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL) 

import plotly.graph_objects as go
import pandas as pd
from plotly.graph_objs import Figure

df = pd.read_csv('wdmonthname.csv')

fig: Figure = go.Figure()

fig.add_trace(go.Violin(x=df['Month'], y=df['Weight'],
                        line_color='rgba(175,69,68,0.5)',
                        )
              )

fig.update_traces(box_visible=True, meanline_visible=True,
                  points='all', pointpos=-0, jitter=0.5,
                  marker_line_color='rgba(0,0,0,0.5)',
                  marker_line_width=1,
                  showlegend=False)

fig.update_layout(template='simple_white')

fig.show()
