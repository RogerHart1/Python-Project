text_file = open("stop-words.txt")
lines = text_file.readlines()

def stopwords(response): 
	response = " " + response
	for word in lines:
		response = response.replace(" " + word[0:-1] + " ", " ")
	return response
	




response = raw_input("What is your name ? ")
response = stopwords(response)
print("Hello " + response)

response = raw_input("what is your favourite band?")
print("I also like "+ response)

response = raw_input("you may like music but what about alcohol, do you like a tipple?")
if(response == "No"): print("tee total hey?")
elif(response =="yes"): print("MMMMmmmmmmm")

drink = ("beer","vodka", "ale", "whiskey", "or something else")
#print drink
response = raw_input("If you like alcohol, which one would you choose from the list? beer,vodka, ale, whiskey, or something else")
#print drink")
if(response == drink[0]): print("oh okay a beer drinker")
elif(response == drink[2]): print("very nice, a real kentish drink")
elif(response == drink[3]): print("a true scotsman hey?")
elif(response ==drink[1]): print("okay")
else: print("never heard of that one" + " " + "what about food?")

response = raw_input("what is your favourite food?")
print("cool")

response = raw_input("And do you have a favourite colour, if so what colour would it be?")
colour = ("blue","brown","red","green","black","white","yellow","indigo","purple","pink")
if(response == colour[0]): print("blue like the sky?" + " " + "why blue?")
elif(response == colour[1]): print("brown like muddy water?" + " " + "why brown?")
elif(response ==  colour[2]): print("red like poppie red?" + " " + "why red?") 
elif(response == colour[3]): print("green like the grass?" + " " + "very natural but, why")
elif(response == colour[4]): print("black, as dark as the night" + " " + "Eerie..why black?")
elif(response == colour[5]): print("white, how very neutral" + " " + "why white?")
elif(response == colour[6]): print("yellow, like the sun" + " " + " why yellow")
elif(response == colour[7]): print("Indigo, that's different" + " " + "why indigo")
elif(response == colour[8]): print("purple, I have colours like that in my garden" + " " + "why purple")
elif(response == colour[9]): print("pink, thats quite a girly colour" + " " + "why pink?")
elif(response == colour[10]):print("Never thought of that colour, Why?")

colour_reply = raw_input()
print(colour_reply)

print("each to their own, what else would you like to ask? I maybe able to help!")
more_questions = raw_input(" ")


