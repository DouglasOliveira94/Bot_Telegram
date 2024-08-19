from telethon import TelegramClient, events, sync
import time

# Substitua estes valores com suas credenciais, que podem ser pegas no site da api do telegram
api_id = '' #colocar o api id
api_hash = '' #colocar o api Hash
phone_number = '+55' #colocar o seu numero do telefone com o ddd


client = TelegramClient('session_name', api_id, api_hash)


async def get_group_ids(client):
    group_ids = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            print(f"Group name: {dialog.name}, Group ID: {dialog.id}")
            group_ids.append(dialog.id)
    return group_ids


async def send_messages(client, group_ids):
    # Mensagem a ser enviada
    message = "" #preencha aqui a mensagem a ser enviada
    # Enviando mensagem para cada grupo
    for group_id in group_ids:
        try:
            await client.send_message(group_id, message)
            print(f"Mensagem enviada para o grupo {group_id}")
            time.sleep(2)  # Pausa de 1 segundo entre as mensagens para evitar spam
        except Exception as e:
            print(f"Erro ao enviar mensagem para o grupo {group_id}: {e}")


async def main():
    await client.start(phone=phone_number)

    # Obter IDs dos grupos
    group_ids = await get_group_ids(client)
    print(group_ids)

    # Enviar mensagens
    await send_messages(client, group_ids)

with client:
    client.loop.run_until_complete(main())

client.disconnect()
