from GameState import ProcessGameState

def main():
    state = ProcessGameState("game_state_frame_data.parquet")
    # print(state.dataFrame.inventory)
    # for thing in state.dataFrame.loc[0, "inventory"]:
        # print(thing, type(thing))

    # print(state.dataFrame.iloc[0, :])
        
    
if __name__ == "__main__":
    main()