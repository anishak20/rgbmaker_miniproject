from rgbmaker.imgplt import save_fig
from matplotlib import pyplot as plt

class RGBC:
  def __init__(self, position, radius, svy, cmin, lvl, kind='png'):
    pass
  
  def plot(self):
    plt.ioff()
    fig = plt.figure(figsize=(20, 20))
    rows,columns, i = 1,1,1
    
    ax = fig.add_subplot(rows, columns, i, projection=wcs)
    if len(self.svy)==1:
      pass

    return save_fig(plt, fig, kind=self.kind, output='output.jpg')
