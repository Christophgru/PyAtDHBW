"""
player-class-file
"""


class Player:
    """
    player-class
    """

    def __init__(self, isreal: bool, name: str):
        self.isreal: bool = isreal
        self.name: str = name

    def choosediceorcheck(self, dicedict, _ui, activeplayer):
        """

        @param dicedict:
        @type dicedict:
        @param _ui:
        @type _ui:
        @param activeplayer:
        @type activeplayer:
        @return:
        @rtype:
        """
        if activeplayer == 1 and not self.isreal:
            _ui.choosediceorcheck(dicedict, "1\n1\n")
        else:
            _ui.choosediceorcheck(dicedict)

    def choose_action_with_dice_arr(self, params: dict):
        """

        @param mocked_input:
        @param params:
        @return:
        """
        if params["activeplayer"] == 1 and not self.isreal:
            options: list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16]
            choice = options[params["nrround"] - 1]
            result = params["ui"].choose_action_with_dice_arr({"dicedict": params["dicedict"],
                                                               "gameblock": params["gameblock"],
                                                               "activeplayer": params["activeplayer"],
                                                               "playernames": [params["player1_name"],
                                                                               self.name],
                                                               "isPVE": True}, choice)
            return result

        return params["ui"].choose_action_with_dice_arr({"dicedict": params["dicedict"],
                                                         "gameblock": params["gameblock"],
                                                         "activeplayer": params["activeplayer"],
                                                         "playernames": [params["player1_name"], self.name],
                                                         "isPVE": False})
