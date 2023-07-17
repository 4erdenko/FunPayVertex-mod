from google_sheets.text_templates.champions_dict import \
    translate_champion_names

start_row = 2
end_row = 20
lvl_mapping = {
    '30': '3️⃣0️⃣',
    '31': '3️⃣1️⃣',
    '32': '3️⃣2️⃣',
    '33': '3️⃣3️⃣',
    '34': '3️⃣4️⃣',
    '35': '3️⃣5️⃣',
    '36': '3️⃣6️⃣',
    '37': '3️⃣7️⃣',
    '38': '3️⃣8️⃣',
    '39': '3️⃣9️⃣',
    '40': '4️⃣0️⃣',
    '50': '5️⃣0️⃣',
}


def create_summary_ru(acc_number, BE, LVL, skins, RP=None):
    LVL = lvl_mapping.get(LVL, LVL)
    skin_lines = skins.split('\n')
    # print(f'skin_lines: {skin_lines}')
    skins_str = ''
    # print(f'skins_str: {skins_str}')
    for skin in skin_lines:
        # print(f'skin: {skin}')
        skin_name = (
            skin.rsplit(None, 1)[-1] if ' ' in skin else skin
        )  # get the last word (champion name)
        # print(f'skin_name: {skin_name}')
        skin_name = translate_champion_names(
            skin_name
        )  # translate the champion name
        temp_str = skins_str + (', ' if skins_str else '') + skin_name
        # print(f'temp_str: {temp_str}')
        # add the new skin_name only if it doesn't exceed the limit
        if len(temp_str) <= (41 if RP else 51):
            skins_str = temp_str
            # print(f'skins_str: {skins_str}')
        else:
            # print(f'break')
            break
    if RP is None:
        # print(f'№{acc_number}🅰️Автовыдача🅰️🔷{BE}BE{LVL}LVL🧾Скины для:{skins_str}')
        return (
            f'№{acc_number}🅰️Автовыдача🅰️🔷{BE}BE{LVL}LVL🧾Скины для:{skins_str}'
        )
    else:
        return f'№{acc_number}🅰️Автовыдача🅰️🔷{BE}BE{LVL} LVL💥350RP💥️🧾Скины для:{skins_str}'


def create_summary_en(acc_number, BE, LVL, skins, RP=None):
    LVL = lvl_mapping.get(LVL, LVL)
    skin_lines = skins.split('\n')
    # print(f'skin_lines: {skin_lines}')
    skins_str = ''
    # print(f'skins_str: {skins_str}')
    for skin in skin_lines:
        # print(f'skin: {skin}')
        skin_name = (
            skin.rsplit(None, 1)[-1] if ' ' in skin else skin
        )  # get the last word (champion name)
        # print(f'skin_name: {skin_name}')
        # skin_name = translate_champion_names(skin_name)  # translate the champion name
        temp_str = skins_str + (', ' if skins_str else '') + skin_name
        # print(f'temp_str: {temp_str}')
        # add the new skin_name only if it doesn't exceed the limit
        if len(temp_str) <= (41 if RP else 51):
            skins_str = temp_str
            # print(f'skins_str: {skins_str}')
        else:
            # print(f'break')
            break
    if RP is None:
        return (
            f'№{acc_number}🅰️AUTO-SALE🅰️🔷{BE}BE{LVL}LVL🧾Skins for:{skins_str}'
        )
    else:
        return (
            f'№{acc_number}🅰️AUTO-SALE🅰️🔷{BE}BE{LVL}LVL💥350RP💥‍'
            f'🧾Skins for:{skins_str}'
        )


def create_description_ru(acc_number, skins, screenshot):
    return (
        f'#{acc_number}#\n'
        f'Привет 🫡 \n'
        f'Этот аккаунт был создан мной. \n'
        f'Прокачан мной, но он с радостью станет твоим😊, \n'
        f'ты поставишь туда свою почту📩, настоящую, \n'
        f'поставишь свой пароль, мощный💪, \n'
        f'и вперёд в ранкеды (✿◠‿◠) \n'
        f' \n'
        f'🧚‍♀️Скинчики на аккаунте: \n'
        f'{skins} \n'
        f' \n'
        f'👓А вот здесь, ты увидишь что есть в инвентаре этого аккаунта  - \n'
        f'{screenshot} \n'
        f' \n'
        f'🔴Итак, ты получаешь: \n'
        f'🟢Аккаунт навсегда \n'
        f'🟢Гарантию от бана (если ты конечно сам его не забанишь скриптами) \n'
        f'🟢Чистую статистику \n'
        f'🟢Кучу эссенции \n'
        f'🟢Поддержку в чате 😉 \n'
        f' \n'
        f'Перед первой игрой не забудьте настроить аккаунт в Practice Tool,'
        f' либо настройте файл PersistedSettings.json только на чтение, '
        f'чтобы настройки с предыдущего аккаунта не сбрасывались. \n'
        f' \n'
        f'Играть в обычные режимы перед рейтинговыми играми, нужно, '
        f'чтобы скрыть статистику игр от других игроков, хотя бы немного.'
    )


def create_description_en(acc_number, skins, screenshot):
    return (
        f'#{acc_number}#\n'
        f'YO! \n'
        f'🧚‍♀️Skins on the account: \n'
        f'{skins} \n'
        f' \n'
        f'👓Screen of hextech - \n'
        f'{screenshot} \n'
        f' \n'
        f'🔴So, you get: \n'
        f'🟢Account with not linked email. \n'
        f'🟢Account forever \n'
        f'🟢Guarantee from ban (if you do not ban it yourself with scripts) \n'
        f'🟢Clean statistics \n'
        f'🟢A lot of essence \n'
        f'🟢Support in chat 😉 \n'
        f' \n'
        f'Before the first game, do not forget to set up an account in the '
        f'Practice Tool, or set the PersistedSettings.json '
        f'file to read only so that the'
        f'Play regular modes before ranked games, you need to hide game stats '
        f'from other players, at least a little bit.'
        f'You can buy an account even if Im offline, '
        f'the account is issued automatically 😉 \n'
    )
