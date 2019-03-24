import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages
fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
#ax3=fig.add_subplot(123)

ax1.scatter(np.linspace(0,1,5),np.linspace(0,5,5))
ax2.bar([6,2],[2,7])
#ax3.axvline(0.65)
ax1.set(title="scatter chart",xlabel="x",ylabel="y")
#ax2.set(title="bar chart",xlabel="x",ylabel="y")
ax2.set_xlim(1,3)
ax2.set_title("bar")

#plt.show()
#plt.savefig("foo.png")
p=PdfPages('multipage.pdf')
p.savefig()
p.close()