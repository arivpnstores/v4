from kyt import *

#CRATE VMESS
@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
	async def create_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Quota:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as pw1:
			await event.respond("**Limit-ip:**")
			pw1 = pw1.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw1 = (await pw1).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Expaired:**")
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
		cmd = f'printf "%s\n" "{user}" "{pw}" "{pw1}" "{exp}" | bot-add-vme'
		citsy = f" cat /etc/xray/city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **Successfully Created**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
#			c = [x.group() for x in re.finditer("Host XrayDNS(.*)",a)]
#			d = [x.group() for x in re.finditer("Pub Key(.*)",a)]
			print(b)
#			print(d)
#			print(c)
#			xx = re.search("Pub Key      :(.*)",d[0]).group(1)
#			xxx = re.search("Host XrayDNS :(.*)",d[0]).group(1)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**🐾🕊️ Xray/Vmess Account 🕊️🐾**
**━━━━━━━━━━━━━━━━━**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» XRAY DNS     :** `{HOST}`
**» User Quota   :** `{pw} GB`
**» Port DNS     :** `443, 53`
**» port TLS     :** `222-1000`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `(/multi path)/vmess`
**» Path NLS     :** `(/multi path)/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**» Pub Key      :** `{PUB}`
**━━━━━━━━━━━━━━━━━**
**» Link TLS     :** 
``{b[0].strip("'").replace(" ","")}``
**━━━━━━━━━━━━━━━━━**
**» Link NTLS    :** 
``{b[1].strip("'").replace(" ","")}``
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/vmess-{user}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@ARI_VPN_STORE**

``
◇━━━━━━━━━━━━━━━━━◇
*_PEMBELIAN BERHASIL_*
◇━━━━━━━━━━━━━━━━━◇
-» PRODUK : VMESS
-» REGION : {city.strip()}
-» REQ CONFIG : 
-» REQ NAMA : {user.strip()}
-» DEVICE : 1 IP
-» HARGA : 
-» AKTIF : {exp} HARI
-» TGL EXP : {later}
◇━━━━━━━━━━━━━━━━━◇
*_ARI STORE_*
``
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# TRIAL VMESS
@bot.on(events.CallbackQuery(data=b'trial-vmess'))
async def trial_vmess(event):
	async def trial_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Minutes:**")
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
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{exp}" | bot-trial-vme'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User Trial Successfully Created**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
			print(b)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**🐾🕊️ Xray/Vmess Account 🕊️🐾**
**━━━━━━━━━━━━━━━━━**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» XRAY DNS     :** `{HOST}`
**» User Quota   :** `Unlimited`
**» Port DNS     :** `443, 53`
**» port TLS     :** `222-1000`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `(/multi path)/vmess`
**» Path NLS     :** `(/multi path)/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**» Pub Key      :** `{PUB}`
**━━━━━━━━━━━━━━━━━**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/vmess-{z["ps"]}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@ARI_VPN_STORE**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
#LOCK VMESS
@bot.on(events.CallbackQuery(data=b'lock-vmess'))
async def lock_vmess(event):
	async def lock_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username:**")
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
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{exp}" | bot-lock-vm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Locked**")
		else:
			msg = f"""**Successfully Locked**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await lock_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
#UNLOCK VMESS
@bot.on(events.CallbackQuery(data=b'unlock-vmess'))
async def unlock_vmess(event):
	async def unlock_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Username:**")
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
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{exp}" | bot-unlock-vm'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{exp}` **Successfully Unlock**")
		else:
			msg = f"""**Successfully Locked**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await unlock_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
#CEK VMESS
@bot.on(events.CallbackQuery(data=b'cek-vmess'))
async def cek_vmess(event):
	async def cek_vmess_(event):
		cmd = 'bot-cek-ws'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Vmess**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vmess'))
async def delete_vmess(event):
	async def delete_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | bot-del-vme'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **Successfully Deleted**")
		else:
			msg = f"""**Successfully Deleted**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
	async def vmess_(event):
		inline = [
[Button.inline(" TRIAL VMESS ","trial-vmess"),
Button.inline(" CREATE VMESS ","create-vmess")],
[Button.inline(" CHECK VMESS ","cek-vmess"),
Button.inline(" DELETE VMESS ","delete-vmess")],
[Button.inline(" LOCK VMESS ","lock-vmess"),
Button.inline(" UNLOCK VMESS ","unlock-vmess")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**🐾🕊️ VMESS MANAGER 🕊️🐾**
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 **» Service:** `VMESS`
🔰 **» Hostname/IP:** `{DOMAIN}`
🔰 **» ISP:** `{z["isp"]}`
🔰 **» Country:** `{z["country"]}`
🤖 **» @ARI_VPN_STORE**
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)