import matplotlib.pyplot as plt

squares = [1,4,9,16,25];
plt.plot(squares);
plt.title('squares numbers',fontsize = 20);
plt.xlabel('value',fontsize = 14);
plt.ylabel('squares of value',fontsize = 14);
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()

