from .. import udB

try:
    eval(udB.get("ASST_CMDS"))
except BaseException:
    udB.set("ASST_CMDS", "{}")


def add_cmd(cmd, msg, media):
    ok = eval(udB.get("ASST_CMDS"))
    ok.update({cmd: {"msg": msg, "media": media}})
    return udB.set("ASST_CMDS", str(ok))


def rem_cmd(cmd):
    ok = eval(udB.get("ASST_CMDS"))
    if ok.get(cmd):
        ok.pop(cmd)
        return udB.set("ASST_CMDS", str(ok))
    return


def cmd_reply(cmd):
    ok = eval(udB.get("ASST_CMDS"))
    if ok.get(cmd):
        okk = ok[cmd]
        return okk["msg"], okk["media"]
    return


def list_cmds():
    ok = eval(udB.get("ASST_CMDS"))
    if ok.keys():
        return ok.keys()
    return
