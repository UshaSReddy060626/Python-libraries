#pie chart
import matplotlib.pyplot as plt
subjects=["math","science","social","English"]
students=[89,75,95,67]
plt.pie(students)
plt.show()

#labels
plt.pie(students,labels=subjects)
plt.show()

#autopct
plt.pie(
    students,
    labels=subjects,
    autopct="%1.1f%%"
)
plt.show()

#explode
explode=[0.1,0,0,0]
plt.pie(
    students,
    labels=subjects,
    explode=explode,
    autopct="%1.1f%%"
)
plt.show()


#subplot
x=[1,2,3,4]
y=[10,20,15,25]
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Line Plot")
plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("Bar Chart")
plt.tight_layout()
plt.show()


#subplots
x=[1,2,3,4]
y=[10,20,15,25]
fig,ax=plt.subplots(1,2,figsize=(10,4))
ax[0].plot(x,y)
ax[0].set_title("Line Plot")
ax[1].bar(x,y)
ax[1].set_title("Bar Chart")
plt.tight_layout()
plt.show()

#axis customization
#xlim()
#ylim()
#xticks()
#yticks()
x=[1,2,3,4]
y=[20,40,60,80]
plt.plot(x,y)
plt.xlim(1,4)
plt.ylim(0,100)
plt.xticks([1,2,3,4])
plt.yticks([0,20,40,60,80,100])
plt.grid()
plt.show()

#figure size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot([1, 2, 3], [1, 4, 9])
ax2.plot([1, 2, 3], [9, 4, 1])
plt.show()

#styles different markers
x = [1,2,3,4]
y = [10,20,30,40]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 3))
ax1.plot(x, y, marker='o')  
ax1.set_title('Circle')
ax2.plot(x, y, marker='s')
ax2.set_title('Square')
ax3.plot(x, y, marker='^') 
ax3.set_title('Triangle')
plt.tight_layout()
plt.show()

#different line styles
x = [1, 2, 3, 4]
y = [2, 4, 1, 5]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 3))
ax1.plot(x, y, linestyle='-')  
ax1.set_title('Solid')
ax2.plot(x, y, linestyle='--')  
ax2.set_title('Dashed')
ax3.plot(x, y, linestyle=':')
ax3.set_title('Dotted')
plt.tight_layout()
plt.show()

