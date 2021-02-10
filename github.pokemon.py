def pokemon_centering(Top_Centering, Bottom_Centering, Left_Centering, Right_Centering):
  Top_Bottom_Skew = Top_Centering +    Bottom_Centering 
  Left_Right_Skew = Left_Centering + Right_Centering
  Top_Cen_Post_Skew = Top_Centering/Top_Bottom_Skew 
  Bottom_Cen_Post_Skew = Bottom_Centering/Top_Bottom_Skew
  Left_Cen_Post_Skew = Left_Centering/ Left_Right_Skew 
  Right_Cen_Post_Skew = Right_Centering/Left_Right_Skew 
  Correct_Top_Measure = str (Top_Cen_Post_Skew*100) + "%"
  Correct_Bottom_Measure = str (Bottom_Cen_Post_Skew*100) + "%"
  Correct_Left_Measure = str (Left_Cen_Post_Skew*100) + "%"
  Correct_Right_Measure = str (Right_Cen_Post_Skew*100) + "%"
  TB_ret = Correct_Top_Measure, Correct_Bottom_Measure
  LR_ret = Correct_Left_Measure, Correct_Right_Measure
  return TB_ret, LR_ret
  

  
TB_ret, LR_ret = pokemon_centering(2.5, 2.6, 2.2, 2.3)
print(f"The top to bottom centering for this card is: {TB_ret}")
print(f"The left to right centering for this card is: {LR_ret}")
