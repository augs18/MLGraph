#Formula obtained for the trained model
Def graph(formula, x_range):
  x=np.array(x_range)
  y=eval(formula)
  plt.plot(x,y)
 
#Plotting the prediction line
graph('rear.coef_*x+regr.intercept_,range(1000,2700))
plt.scatter(size,house_price,color=red)
plt.ylabel('House Price')
plt.xlabel('size of House')
plt.show


