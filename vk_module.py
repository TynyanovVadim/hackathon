import requests

def vk_user(user_id):
    check = requests.get("https://vk.com/" + user_id)
    check2 = requests.get(
        "https://api.vk.com/method/utils.resolveScreenName?screen_name=" + user_id + "&access_token=vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ&v=5.154")
    data_check2 = check2.json()
    if (check.status_code == 404):
        return "Пользователь не найден!"
    elif (data_check2['response']['type'] != "user"):
        return "Данный id не является пользователем!"
    else:
        method = "https://api.vk.com/method/users.get"
        user_id = "user_ids=" + user_id
        access_token = "access_token=vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ"
        fields = "fields=id,first_name,last_name,country,city,sex,bdate"
        version = "v=5.154"
        result = method + "?" + user_id + "&" + fields + "&" + access_token + "&" + version

        response = requests.get(result)
        data = response.json()
        return data

def vk_group(group_id):
    check = requests.get("https://vk.com/" + group_id)
    check2 = requests.get("https://api.vk.com/method/utils.resolveScreenName?screen_name=" + group_id + "&access_token=vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ&v=5.154")
    data_check2 = check2.json()
    if (check.status_code == 404):
        return "Группа не найдена!"
    elif (data_check2['response']['type'] != "group" and data_check2['response']['type'] != "page"):
        return "Данный id не является группой!"
    else:
        method = "https://api.vk.com/method/groups.getById"
        group_id = "group_id=" + group_id
        access_token = "access_token=vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ"
        version = "v=5.154"
        fields = "fields=id,name,screen_name,type,country,city,description,wiki_page"
        result = method + "?" + group_id + "&" + fields + "&" + access_token + "&" + version

        response = requests.get(result)
        data = response.json()
        return data

def vk_user_execute(user_id):
    check = requests.get("https://vk.com/" + user_id)
    check2 = requests.get("https://api.vk.com/method/utils.resolveScreenName?screen_name=" + user_id + "&access_token=vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ&v=5.154")
    data_check2 = check2.json()
    if (check.status_code == 404):
        return "Пользователь не найден!"
    elif (data_check2['response']['type'] != "user"):
        return "Данный id не является пользователем!"
    else:
        method = "https://api.vk.com/method/execute"
        access_token = "vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ"
        version = "5.154"
        fields = "id,first_name,last_name,country,city,sex,bdate"
        code = "var info = API.users.get({\"user_ids\": \"" + user_id + "\", \"fields\": \"" + fields + "\"}); return info;"

        response = requests.post(method,
                                 data={
                                     "code": code,
                                     "access_token": access_token,
                                     "v": version,
                                 })

        data = response.json()
        return data

def get_by_id(id):
    check = requests.get("https://vk.com/" + id)
    check2 = requests.get("https://api.vk.com/method/utils.resolveScreenName?screen_name=" + id + "&access_token=vk1.a.yV-2guVAe7Lz6aBJHZEXKC18hPFnxNkw_Dm7jc2WJZHlWvR-khoHtmKos2_wK8mFPqoPcZIz2Q0mVDNL4O3PM9r1qPDpt0Si2wZf0cRxBsw4XZSx177rpaH3VwIE-fe2b0fjDZmAncPgekncp9YMWya_DdaFBaovYd3mu41UwTDeHVqhes72HwBWyu-aUzAlWrvE135cuBv531TUYrKQtQ&v=5.154")
    data_check2 = check2.json()
    if (check.status_code == 404):
        return "Пользователь не найден!"
    elif (data_check2['response']['type'] == "user"):
        return vk_user(id)
    return vk_group(id)
