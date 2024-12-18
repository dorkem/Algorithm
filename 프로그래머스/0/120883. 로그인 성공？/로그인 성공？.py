def solution(id_pw, db):
    answer = ""
    id = [i[0] for i in db]

    if id_pw in db:
        answer = "login"
    elif id_pw[0] not in id:
        answer = "fail"
    else:
        answer = "wrong pw"
    return answer