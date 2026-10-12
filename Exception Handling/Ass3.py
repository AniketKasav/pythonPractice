'''Q3. List Index Error
Create a list of five numbers. Ask the user to enter an index and display the corresponding element. Handle an invalid index.'''

list=(1,5,8,6,9)

try:
    print("Enter a index of list to display the number : ")
    idx=int(input())
    print("Number is : ",list[idx])
except IndexError as e:
    print("Index is not valid ")