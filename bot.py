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
        await bot.say("Added " + (arg) + " point(s) to team black!")
        global atotal
        if atotal == 0:
            atotal = float(arg)
        else:
            atotal += float(arg)

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
        await bot.say("Added " + (arg) + " point(s) to team white!")
        global btotal
        if btotal == 0:
            btotal = float(arg)
        else:
            btotal += float(arg)

#SHOWS POINTS OF TEAM 1
@bot.command(pass_context=True)
async def teamwhite(ctx):
    global btotal
    await bot.say("This team has {} points.".format(btotal))



#--------------------------------------------------------------------------












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
    role = ((discord.utils.get(user.server.roles, name="Team Black")), (discord.utils.get(user.server.roles, name="Team White")))
    await bot.add_roles(user, random.choice(role))


bot.run("NDYzNzk3MDM4MjI0NTA2OTIw.Dh5fJw.joqORD_VFra55H1L5q23CKKj1VE")
