import znc


class pyawaynick(znc.Module):
    module_types = [znc.CModInfo.UserModule]

    away_nick_timer = None
    back_nick_timer = None

    def OnClientLogin(self):
        self.GetNetwork().PutIRC("NICK " + self.GetNetwork().GetNick())

    def OnClientDisconnect(self):
        if not self.GetNetwork().IsUserAttached():
            if "away_nick" in self.nv:
                self.GetNetwork().PutIRC("NICK " + self.nv["away_nick"])

    def OnModCommand(self, sCommand):
        sCommand = sCommand.split(" ")
        sParams = sCommand[1:]
        sCommand = sCommand[0].lower()

        if sCommand == "set":
            self.nv["away_nick"] = sParams[0]
            self.PutModule("Your away nick is now set to: '" + sParams[0] + "'")
        elif sCommand == "show":
            if not "away_nick" in self.nv:
                self.PutModule("You have no away nick set - use the SET command")
            else:
                self.PutModule("Your away nick is set to: '" + self.nv["away_nick"] + "'")
