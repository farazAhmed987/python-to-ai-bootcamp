message = "hello im akif"

print(message[2])
print(message[-1])

print(message[0:5])

print(message)

# string_name[start : stop]

# methods
print(message.upper())
print(message.title())

st = "   a    "
print(st.strip())
print(st.lstrip())
print(st.rstrip())

print(message.replace("hello", "Hey!"))

s = "a,b,c"
print(s.split(","))

// practice

message = "  python to ai bootcamp  "

clean_message = message.strip()

print("Original:", repr(message))
print("Cleaned:", clean_message)
print("Uppercase:", clean_message.upper())
print("Title Case:", clean_message.title())
print("First Five Characters:", clean_message[:5])
print("Last Character:", clean_message[-1])
print("Replaced Text:", clean_message.replace("ai", "AI"))

topics = "Python,NumPy,Pandas,Machine Learning"
topic_list = topics.split(",")

print("Topics:", topic_list)
print("Number of Topics:", len(topic_list))

for topic in topic_list:
    print("-", topic.strip().title())
