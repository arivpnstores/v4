from kyt import *

@bot.on(events.CallbackQuery(data=b'regip'))
async def reg_ip(event):
	async def reg_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**VERIFIKASI ADMIN:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as dom:
			await event.respond('**IP VPS:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		async with bot.conversation(chat) as sub:
			await event.respond('**NAMA CLIENT:**')
			sub = sub.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			sub = (await sub).raw_text
		async with bot.conversation(chat) as ipvps:
			await event.respond('**EXPAIRED:**')
			ipvps = ipvps.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			ipvps = (await ipvps).raw_text
		cmd = f'printf "%s\n" "{user}" "{dom}" "{sub}" "{ipvps}"  | bot-add-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Register IP**")
		else:
			msg = f"""**Successfully Register Ip {dom}**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await reg_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'renip'))
async def renip(event):
	async def renip_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**VERIFIKASI ADMIN:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as dom:
			await event.respond('**IP VPS:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		async with bot.conversation(chat) as ipvps:
			await event.respond('**EXPAIRED:**')
			ipvps = ipvps.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			ipvps = (await ipvps).raw_text
		cmd = f'printf "%s\n" "{user}" "{dom}" "{ipvps}"  | bot-renew-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Renew IP**")
		else:
			msg = f"""**Successfully Renew Ip {dom}**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delip'))
async def delip(event):
	async def delip_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**VERIFIKASI ADMIN:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as dom:
			await event.respond('**IP VPS:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		cmd = f'printf "%s\n" "{user}" "{dom}" | bot-del-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Delete IP**")
		else:
			msg = f"""**Successfully Delete Ip {dom}**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)


@bot.on(events.CallbackQuery(data=b'reg'))
async def reg(event):
	async def reg_(event):
		inline = [
[Button.inline(" ADD IP ","regip"),
Button.inline(" DELETE IP ","delip")],
[Button.inline(" RENEW IP ","renip"),
Button.inline(" MENU ","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🐾🕊️ PREMIUM PANEL MENU 🕊️🐾**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 **» Hostname/IP:** `{DOMAIN}`
🔰 **» ISP:** `{z["isp"]}`
🔰 **» Country:** `{z["country"]}`
🤖 **»@ARI_VPN_STORE**
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await reg_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'reboot'))
async def rebooot(event):
	async def rebooot_(event):
		cmd = f'reboot'
		time.sleep(1)
		await event.edit("`Processing Restart Service Server...`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		subprocess.check_output(cmd, shell=True)
		await event.edit(f"""
**» REBOOT SERVER**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await rebooot_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'resx'))
async def resx(event):
	async def resx_(event):
		cmd = f'systemctl restart xray | systemctl restart nginx | systemctl restart haproxy | systemctl restart server | systemctl restart udp-custom | systemctl restart noobzvpns | systemctl restart client'
		subprocess.check_output(cmd, shell=True)

		time.sleep(1)
		await event.edit("`Processing Restart Service Server...`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(1)
		await event.edit(f"""
```Processing... 100%\n█████████████████████████ ```
**» Restarting Service Done**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await resx_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'speedtest'))
async def speedtest(event):
	async def speedtest_(event):
		cmd = 'speedtest-cli --share'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		time.sleep(0)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		await event.respond(f"""
**
{z}
**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await speedtest_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'backup'))
async def backup(event):
    async def backup_(event):
        cmd = 'backup-bot'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Not Exist**")
        else:
            msg = f"""
```{a}```
**» 🤖@ARI_VPN_STORE**
"""
            await event.respond(msg)
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await backup_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'restore'))
async def restore(event):
    async def restore_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**File ID   :**')
            file_id_event = await user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            file_id = file_id_event.raw_text
            
            await event.respond('**File Path :**')
            file_path_event = await user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            file_path = file_path_event.raw_text
            
        cmd = f'printf "%s\n%s\n" "{file_id}" "{file_path}" | restore-bot'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Link Not Exist**")
        else:
            msg = f"""```{a}```
**🤖@ARI_VPN_STORE**
"""
            await event.respond(msg)
    
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await restore_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'point'))
async def point(event):
	async def point_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**VERIFIKASI ADMIN:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**DOMAIN:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as pw1:
			await event.respond("**SUB DOMAIN:**")
			pw1 = pw1.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw1 = (await pw1).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**IP-VPS:**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text

		time.sleep(1)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{pw}" "{pw1}" "{exp}" | bot-cf'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond(f"**VPS** `{exp}` **Successfully Pointing**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await point_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
@bot.on(events.CallbackQuery(data=b'backer'))
async def backers(event):
	async def backers_(event):
		inline = [
[Button.inline(" BACKUP","backup"),
Button.inline(" RESTORE","restore")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🐾🕊️ PREMIUM PANEL MENU 🕊️🐾**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 **» Hostname/IP:** `{DOMAIN}`
🔰 **» ISP:** `{z["isp"]}`
🔰 **» Country:** `{z["country"]}`
🤖 **»@ARI_VPN_STORE**
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backers_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'setting'))
async def settings(event):
	async def settings_(event):
		inline = [
[Button.inline(" SPEEDTEST","speedtest"),
Button.inline(" BACKUP & RESTORE","backer")],
[Button.inline(" REBOOT SERVER","reboot"),
Button.inline(" RESTART SERVICE","resx")],
[Button.inline(" REGIS IP-VPS","reg"),
Button.inline(" POINTING DOMAIN","point")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🐾🕊️ PREMIUM PANEL MENU 🕊️🐾**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 **» Hostname/IP:** `{DOMAIN}`
🔰 **» ISP:** `{z["isp"]}`
🔰 **» Country:** `{z["country"]}`
🤖 **»@ARI_VPN_STORE**
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await settings_(event)
	else:
		await event.answer("Access Denied",alert=True)
