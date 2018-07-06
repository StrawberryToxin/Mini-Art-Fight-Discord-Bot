import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print ("Bot is online and connected to discord")




@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Smol Beans")
    await bot.add_roles(member, role)

#---------------------------------------------------------------------------
#TEAM 1
atotal = float(0)


#AWARDS POINTS FOR TEAM 1
@bot.command(pass_context=True)
async def blackadd(ctx, arg):
    if "MODS" in [y.name.upper() for y in ctx.message.author.roles]:
        await bot.say("Added " + (arg) + " point(s) to team black!")
        global atotal
        if atotal == 0:
            atotal = float(arg)
        else:
            atotal += float(arg)
    else:
        await bot.say("I'm sorry, you cannot use this command.")

#SHOWS POINTS OF TEAM 1
@bot.command(pass_context=True)
async def teamblack(ctx):
    global atotal
    await bot.say("This team has {} points.".format(atotal))

#---------------------------------------------------------------------------

#TEAM 2
btotal = float(0)


#AWARDS POINTS FOR TEAM 1
@bot.command(pass_context=True)
async def whiteadd(ctx, arg):
    if "MODS" in [y.name.upper() for y in ctx.message.author.roles]:
        await bot.say("Added " + (arg) + " point(s) to team white!")
        global btotal
        if btotal == 0:
            btotal = float(arg)
        else:
            btotal += float(arg)
    else:
        await bot.say("I'm sorry, you cannot use this command.")

#SHOWS POINTS OF TEAM 1
@bot.command(pass_context=True)
async def teamwhite(ctx):
    global btotal
    await bot.say("This team has {} points.".format(btotal))



#--------------------------------------------------------------------------
#TEAM ONE ATTACK
#--------------------------------------------------------------------------


@bot.command(pass_context=True)
async def blackattack(ctx):
    await bot.say("(Team black) What is your finished piece?\n 1. Head Shot\n 2. Head to Waist\n 3. Full Body")

@bot.command(pass_context=True)
async def whiteattack(ctx):
    await bot.say("(Team white) What is your finished piece?\n 1. Head Shot\n 2. Head to Waist\n 3. Full Body")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith("(Team black) What is your finished piece?"):
        await bot.add_reaction(message, emoji="1⃣")
        await bot.add_reaction(message, emoji="2⃣")
        await bot.add_reaction(message, emoji="3⃣")
    if message.content.startswith("(Team black) What type of lines did you use?"):
        await bot.add_reaction(message, emoji="1⃣")
        await bot.add_reaction(message, emoji="2⃣")
        await bot.add_reaction(message, emoji="3⃣")
    if message.content.startswith("(Team black) How did you color the piece?"):
        await bot.add_reaction(message, emoji="1⃣")
        await bot.add_reaction(message, emoji="2⃣")
        await bot.add_reaction(message, emoji="3⃣")

    if message.content.startswith("(Team white) What type of lines did you use?"):
        await bot.add_reaction(message, emoji="1⃣")
        await bot.add_reaction(message, emoji="2⃣")
        await bot.add_reaction(message, emoji="3⃣")
    if message.content.startswith("(Team white) What is your finished piece?"):
        await bot.add_reaction(message, emoji="1⃣")
        await bot.add_reaction(message, emoji="2⃣")
        await bot.add_reaction(message, emoji="3⃣")
    if message.content.startswith("(Team white) How did you color the piece?"):
        await bot.add_reaction(message, emoji="1⃣")
        await bot.add_reaction(message, emoji="2⃣")
        await bot.add_reaction(message, emoji="3⃣")



@bot.event
async def on_reaction_add(reaction, user):
    global atotal
    global btotal
    if reaction.message.content.startswith("(Team black) How did you color the piece?"):

        if user.id == "463797038224506920":
            ...
        else:
            if str(reaction.emoji) == ("1⃣"):
                if atotal == 0:
                    atotal = float(25)
                else:
                    atotal += float(25)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "You have successfully added points to your team!")
            if reaction.emoji == ("2⃣"):
                if atotal == 0:
                    atotal = float(50)
                else:
                    atotal += float(50)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "You have successfully added points to your team!")
            if reaction.emoji == ("3⃣"):
                if atotal == 0:
                    atotal = float(100)
                else:
                    atotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "You have successfully added points to your team!")
    if reaction.message.content.startswith("(Team black) What type of lines did you use?"):

        if user.id == "463797038224506920":
            ...
        else:
            if str(reaction.emoji) == ("1⃣"):
                if atotal == 0:
                    atotal = float(25)
                else:
                    atotal += float(25)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team black) How did you color the piece?\n "
                                                                 "1. No Color\n 2. Flat Color\n 3. Shaded Color")
            if reaction.emoji == ("2⃣"):
                if atotal == 0:
                    atotal = float(100)
                else:
                    atotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team black) How did you color the piece?\n "
                                                                 "1. No Color\n 2. Flat Color\n 3. Shaded Color")
            if reaction.emoji == ("3⃣"):
                if atotal == 0:
                    atotal = float(100)
                else:
                    atotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team black) How did you color the piece?\n "
                                                                 "1. No Color\n 2. Flat Color\n 3. Shaded Color")
    if reaction.message.content.startswith("(Team black) What is your finished piece?"):

        if user.id == "463797038224506920":
            ...
        else:
            if str(reaction.emoji) == ("1⃣"):
                if atotal == 0:
                    atotal = float(25)
                else:
                    atotal += float(25)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team black) What type of lines did you use?\n "
                                                                 "1. Sketch\n 2. Clean Lines\n 3. Lineless")
            if reaction.emoji == ("2⃣"):
                if atotal == 0:
                    atotal = float(50)
                else:
                    atotal += float(50)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team black) What type of lines did you use?\n "
                                                                 "1. Sketch\n 2. Clean Lines\n 3. Lineless")
            if reaction.emoji == ("3⃣"):
                if atotal == 0:
                    atotal = float(100)
                else:
                    atotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team black) What type of lines did you use?\n "
                                                                 "1. Sketch\n 2. Clean Lines\n 3. Lineless")
    if reaction.message.content.startswith("(Team white) How did you color the piece?"):

        if user.id == "463797038224506920":
            ...
        else:
            if str(reaction.emoji) == ("1⃣"):
                if btotal == 0:
                    btotal = float(25)
                else:
                    btotal += float(25)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "You have successfully added points to your team!")
            if reaction.emoji == ("2⃣"):
                if btotal == 0:
                    btotal = float(50)
                else:
                    btotal += float(50)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "You have successfully added points to your team!")
            if reaction.emoji == ("3⃣"):
                if btotal == 0:
                    btotal = float(100)
                else:
                    btotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "You have successfully added points to your team!")
    if reaction.message.content.startswith("(Team white) What type of lines did you use?"):

        if user.id == "463797038224506920":
            ...
        else:
            if str(reaction.emoji) == ("1⃣"):
                if btotal == 0:
                    btotal = float(25)
                else:
                    btotal += float(25)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team white) How did you color the piece?\n "
                                                                 "1. No Color\n 2. Flat Color\n 3. Shaded Color")
            if reaction.emoji == ("2⃣"):
                if btotal == 0:
                    btotal = float(100)
                else:
                    btotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team white) How did you color the piece?\n "
                                                                 "1. No Color\n 2. Flat Color\n 3. Shaded Color")
            if reaction.emoji == ("3⃣"):
                if btotal == 0:
                    btotal = float(100)
                else:
                    btotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team white) How did you color the piece?\n "
                                                                 "1. No Color\n 2. Flat Color\n 3. Shaded Color")
    if reaction.message.content.startswith("(Team white) What is your finished piece?"):

        if user.id == "463797038224506920":
            ...
        else:
            if str(reaction.emoji) == ("1⃣"):
                if btotal == 0:
                    btotal = float(25)
                else:
                    btotal += float(25)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team white) What type of lines did you use?\n "
                                                                 "1. Sketch\n 2. Clean Lines\n 3. Lineless")
            if reaction.emoji == ("2⃣"):
                if btotal == 0:
                    btotal = float(50)
                else:
                    btotal += float(50)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team white) What type of lines did you use?\n "
                                                                 "1. Sketch\n 2. Clean Lines\n 3. Lineless")
            if reaction.emoji == ("3⃣"):
                if btotal == 0:
                    btotal = float(100)
                else:
                    btotal += float(100)
                await bot.delete_message(reaction.message)
                await bot.send_message(reaction.message.channel, "(Team white) What type of lines did you use?\n "
                                                                 "1. Sketch\n 2. Clean Lines\n 3. Lineless")





#SHOWS ATTACK POINTS
@bot.command(pass_context=True)
async def attackpoints(ctx):
    await bot.say("----\n"
                  "Amount of Character Drawn\n"
                  "----\n"
                  "Head = 25\n"
                  "Head to Waist = 50\n"
                  "Full Body = 100\n"
                  "----\n"
                  "Type of Lines\n"
                  "----\n"
                  "Sketch = 25\n"
                  "Clean Lineart = 100\n"
                  "Lineless = 100\n"
                  "----\n"
                  "Color\n"
                  "----\n"
                  "No Color = 25\n"
                  "Flat Color = 50\n"
                  "Shaded Color = 100\n"
                  "----\n"
                  "To add points to your team, type !(team)add(amount of points) without the () and no spacing!")


@bot.command(pass_context=True)
async def assignteam(ctx):
    user = ctx.message.author
    if "TEAM WHITE" in [y.name.upper() for y in ctx.message.author.roles] or "TEAM BLACK" in [y.name.upper() for y in ctx.message.author.roles]:
        await bot.say("I'm sorry, you cannot use this command right now!")
    else:
        role = ((discord.utils.get(user.server.roles, name="Team Black")), (discord.utils.get(user.server.roles, name="Team White")))
        await bot.add_roles(user, random.choice(role))


bot.run("NDYzNzk3MDM4MjI0NTA2OTIw.Dh5fJw.joqORD_VFra55H1L5q23CKKj1VE")
