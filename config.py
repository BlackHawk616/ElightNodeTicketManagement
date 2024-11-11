#--------Ticket-Bot Config File--------#
#Created by WebTheDev#

#PLACE THE TOKEN FOR THE BOT IN THE TOKEN.JSON FILE!!!!#

import json

#Main Config:#
botStatusType = 'Watching'                                                   #Bot Status Type (Ex. Playing, Watching, Listening, or Streaming)
botStatusMessage = 'Tickets'                                                #The message that is shown on the bots activity
guildID = 1217800505934352485                                           #ID of the Guild the the bot is running in
ticketLogsChannelID = 1300509835250634817                                 #ID of the Channel to send system logs to
ticketTranscriptChannelID = 1300509835250634817                      #ID of the Channel to send ticket transcripts to
databaseName = 'tickets.db'                                          #Leave set to default value unless if you want to use a different database name
debugLogSendID = 1111560053334487131                                     #ID of the Bot Owner to send debug information to

#Ticket Creation/Options Config:#
IDOfChannelToSendTicketCreationEmbed = 1299383770528481297    #ID of the Channel to send the Create a ticket embed to
IDofMessageForTicketCreation = 1305177021978120353                       #This variable was automatically adjusted.
activeTicketsCategoryID = 1299383727784333353                      #ID of the active tickets category
onHoldTicketsCategoryID = 1299383735778545827                             #ID of the onhold tickets category
archivedTicketsCategoryID = 1299383739285246055                    #ID of the archived tickets category

OptionsDict = {
    "Option 1": ("Purchase 💲", "purchase", "Create a Purchase related ticket."),                                      #This is the ticket options dictionary. It defines the different types of tickets that users can create.
    "Option 2": ("Support ❓", "support", "Create a support related ticket."),                                #A ticket option definition should look something like this:  
    "Option 3": ("Sponsorship 💰", "sponsor", "Create a ticket to speak with Management team about sponsorship.")                    #"Option #": ("Title of Option", "Type of Option", "Description of Option")
}                                                                                                             #Add a comma after every option definition except for the last one. 
                                                                                                              #If you only have one option then no comma is needed.
                                                                                                                 

channelPerms = {                                                                                          #This is the ticket channel perms dictionary.
    "purchase": (1299393336934662206,1299390900362940480,),                                                                     #This dictionary defines what roles will have access to each type of Ticket Channel
    "support": (1299393336934662206,1299390900362940480),                                           #Each type can support multiple role IDS
    "sponsor": (1299393336934662206,1299390900362940480)                                              #Each entry into the definition should look something like this:
}                                                                                                         #"Type of Option":(ROLEID1, ROLEID2)
                                                                                                          #Add a comma after every option definition except for the last one. 
                                                                                                          #If you only have one option then no comma is needed.
                                                                                                          #IMPORTANT: MAKE SURE THAT THE TYPE OF OPTION IS THE SAME AS THE TYPE OF OPTION THAT WAS
                                                                                                          #DEFINED IN THE TICKET OPTIONS DEFINITION
                                                                                                          #IF NOT, PERMISSIONS WILL NOT BE SET CORRECTLY AND THE BOT WILL NOT WORK RIGHT.


ticketTypeAllowedToCreatePrivateChannels = "staff"                         #Set this to be the type of option (roles) as defined in the ticket channel perms dictionary that can use the /create command.
multipleTicketsAllowed = False                                             #Set this to True if you would like members to be able to have multiple tickets open at once (otherwise set to False).
dmTicketCopies = True                                                      #Set this to True if you would like the bot to dm Ticket Creators transcript copies of their ticket.


#Embed Config:#
footerOfEmbeds = ''                                                        #Set a custom embed footer of all embedded messages here!
embedColor = 0xffffff                                                      #Set a custom hex color code for all embeds! Make sure to keep the 0x!


def get_token():                                                    
    tokenFile = open("./token.json")                                       #This definition pulls the token from the token.json file
    data = json.loads(tokenFile.read())                                    #Make sure to put your token in the token.json file where it says "PLACETOKENHERE"!                                     
    return (data['BotToken'])


firstRun = False               #This variable was automatically adjusted.



#Please create a new issue on github if you are having issues with using the bot or find any bugs!