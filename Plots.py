import matplotlib.pyplot as plt
from data import Date, Open, High, Low, Close, Adj_Close, Volume
import os
import time

# Color Schema of the Charts
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#D04545", "#F87531", "#A2C257", "#20B2AA", "#4682B4", "#7995EA", "#FF99CC"])
folder_name = 'stock_analysis' + time.strftime("%Y_%m_%d_%H_%M_%S")
path = os.path.join('ANALYSIS', folder_name)
os.mkdir(path)

# Creating a Bar Chart
fig1, ax1 = plt.subplots(figsize=(20, 15))
ax1.bar(Date['Date'], Adj_Close['Adj_Close'])
pos = ax1.get_position()
pos.x0 += 0.05
pos.y0 += 0.07
ax1.set_position(pos)
plt.xticks(fontsize=8, rotation=90, fontweight="bold")
plt.yticks(fontsize=8, fontweight="bold")
ax1.set_title("\nDate-Wise Adjoint Closing Price of the Stock\n")
ax1.set_xlabel("Date", labelpad=20)
ax1.set_ylabel("Closing_Price", labelpad=20)
path = os.path.join('ANALYSIS', folder_name, "fig1.png")
plt.savefig(path)
plt.show()

# Creating a Hortizontal Bar Chart
fig2, ax2 = plt.subplots(figsize=(20, 15))
ax2.barh(Date['Date'], Open['Open'], height=0.95,
         label="Opening", color="orange", align="center")
ax2.barh(Date['Date'], Close['Close'], height=0.60,
         label="Closing", color="blue", align="edge")
pos = ax2.get_position()
pos.x0 += 0.08
pos.y0 += 0.19
ax2.set_position(pos)
plt.xticks(fontsize=8, rotation=90, fontweight="bold")
plt.yticks(fontsize=8, fontweight="bold")
ax2.tick_params(axis="x", pad=10)
ax2.tick_params(axis="y", pad=10)
ax2.set_xlabel("STOCK OPENING & CLOSING", labelpad=40)
ax2.set_ylabel("DATE", labelpad=40)
ax2.legend()
path = os.path.join('ANALYSIS', folder_name, "fig2.png")
plt.savefig(path)
plt.show()

# Pie Chart
fig3, ax3 = plt.subplots()
ResH = []
ResL = []
ResV = []
sum1 = 0
sum2 = 0
sum3 = 0
for j, i, k, v in zip(Date['Date'], High['High'], Low['Low'], Volume['Volume']):
    days = int(j[-2:])
    if days % 30 == 0 or days % 31 == 0:
        ResL.append(sum2//2)
        ResV.append(sum3//2)
        ResH.append(sum1//2)
        sum1 = 0
        sum2 = 0
        sum3 = 0
    else:
        sum1 += float(i)
        sum2 += float(k)
        sum3 += float(v)
ResH.append(sum1//2)
ResL.append(sum2//2)
ResV.append(sum3//2)
data = ResH+ResL+ResV
ax3.pie(data, labels=['High']*len(ResH)+['Low']*len(ResL)+['Volume']*len(ResV))
ax3.set_title("AVG of HIGH,LOW AND VOLUME OF THE STOCK")
path = os.path.join('ANALYSIS', folder_name, "fig3.png")
plt.savefig(path)
plt.show()

# Line Chart
fig4, ax4 = plt.subplots(figsize=(20, 15))
ax4.plot(list(Date['Date']), list(Adj_Close['Adj_Close']), color="green")
pos1 = ax4.get_position()
pos1.x0 += 0.05
pos1.y0 += 0.08
ax4.set_position(pos1)
ax4.tick_params(axis="x", pad=10)
ax4.tick_params(axis="y", pad=10)
plt.xticks(fontsize=8, rotation=90, fontweight="bold")
plt.yticks(fontsize=8, fontweight="bold")
ax4.set_title("ADJOINT_CLOSING")
ax4.set_xlabel("Date", labelpad=10)
ax4.set_ylabel("ADJ_CLOSING VALUE", labelpad=10)
path = os.path.join('ANALYSIS', folder_name, "fig4.png")
plt.savefig(path)
plt.show()

# Area Chart
fig5, ax5 = plt.subplots(figsize=(20, 15))
ax5.fill_between(Date['Date'], Volume['Volume'], color="lightblue")
ax5.set_title("Date vs Volume of the Stock")
ax5.set_xlabel("Date")
ax5.set_ylabel("Volume")
pos1 = ax4.get_position()
pos1.x0 += 0.05
pos1.y0 += 0.08
ax4.set_position(pos1)
ax4.tick_params(axis="x", pad=10)
ax4.tick_params(axis="y", pad=10)
plt.xticks(fontsize=8, rotation=90, fontweight="bold")
plt.yticks(fontsize=8, fontweight="bold")
path = os.path.join('ANALYSIS', folder_name, "fig5.png")
plt.savefig(path)
plt.show()
