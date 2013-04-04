import yaml

def hex_to_rgb(number):
  number = min(0xFFFFFF, max(number, 0))
  b = number % 0x100
  number = (number - b) / 0x100

  g = number % 0x100
  r = (number - g) / 0x100

  return r / 255.0, g / 255.0, b / 255.0

def denormalize(color):
  return min(0xFF, int(0x100 * color))

def to_tk(color):
  r, g, b = (denormalize(c) for c in color)
  return '#%02x%02x%02x' % (r, g, b)

def to_color(color):
  if isinstance(color, (tuple, list)):
    return color
  if isinstance(color, int):
    return hex_to_rgb(color)
  try:
    col = color.lower().replace(' ', '')
    if col.startswith('#'):
      return hex_to_rgb(int(col[1:], 16))
    elif col.startswith('0x'):
      return hex_to_rgb(int(color[2:], 16))
    else:
      result = COLORS.get(col)
      if result:
        return result[1]
  except AttributeError:
    pass

  raise Exception("Didn't understand color name %s." % color)

def _invert(table_in):
  table_out = {}
  for name, value in table_in.itervalues():
    table_out.setdefault(name, []).append(value)
  return table_out

def _load_colors(s):
  table = yaml.safe_load(s)
  inverse = {}
  for entry in table.itervalues():
    name, value = entry
    value = hex_to_rgb(value)

    entry[1] = value
    inverse.setdefault(value, []).append(name)
  return table, inverse

COLORS, INVERSE_COLORS = _load_colors("""
aliceblue: [alice blue, 0xF0F8FF]
antiquewhite1: [antique white 1, 0xFFEFDB]
antiquewhite2: [antique white 2, 0xEEDFCC]
antiquewhite3: [antique white 3, 0xCDC0B0]
antiquewhite4: [antique white 4, 0x8B8378]
antiquewhite: [antique white, 0xFAEBD7]
aqua: [aqua, 0x00FFFF]
aquamarine1: [aquamarine 1, 0x7FFFD4]
aquamarine2: [aquamarine 2, 0x76EEC6]
aquamarine3: [aquamarine 3, 0x66CDAA]
aquamarine4: [aquamarine 4, 0x458B74]
aquamarine: [aquamarine, 0x7FFFD4]
azure1: [azure 1, 0xF0FFFF]
azure2: [azure 2, 0xE0EEEE]
azure3: [azure 3, 0xC1CDCD]
azure4: [azure 4, 0x838B8B]
azure: [azure, 0xF0FFFF]
banana: [banana, 0xE3CF57]
beige: [beige, 0xF5F5DC]
bisque1: [bisque 1, 0xFFE4C4]
bisque2: [bisque 2, 0xEED5B7]
bisque3: [bisque 3, 0xCDB79E]
bisque4: [bisque 4, 0x8B7D6B]
bisque: [bisque, 0xFFE4C4]
black: [black, 0x000000]
blanchedalmond: [blanched almond, 0xFFEBCD]
blue2: [blue 2, 0x0000EE]
blue3: [blue 3, 0x0000CD]
blue4: [blue 4, 0x00008B]
blue: [blue, 0x0000FF]
blueviolet: [blue violet, 0x8A2BE2]
brick: [brick, 0x9C661F]
brown1: [brown 1, 0xFF4040]
brown2: [brown 2, 0xEE3B3B]
brown3: [brown 3, 0xCD3333]
brown4: [brown 4, 0x8B2323]
brown: [brown, 0xA52A2A]
burlywood1: [burly wood 1, 0xFFD39B]
burlywood2: [burly wood 2, 0xEEC591]
burlywood3: [burly wood 3, 0xCDAA7D]
burlywood4: [burly wood 4, 0x8B7355]
burlywood: [burly wood, 0xDEB887]
burntsienna: [burnt sienna, 0x8A360F]
burntumber: [burnt umber, 0x8A3324]
cadetblue1: [cadet blue 1, 0x98F5FF]
cadetblue2: [cadet blue 2, 0x8EE5EE]
cadetblue3: [cadet blue 3, 0x7AC5CD]
cadetblue4: [cadet blue 4, 0x53868B]
cadetblue: [cadet blue, 0x5F9EA0]
cadmiumorange: [cadmium orange, 0xFF6103]
cadmiumyellow: [cadmium yellow, 0xFF9912]
carrot: [carrot, 0xED9121]
chartreuse1: [chartreuse 1, 0x7FFF00]
chartreuse2: [chartreuse 2, 0x76EE00]
chartreuse3: [chartreuse 3, 0x66CD00]
chartreuse4: [chartreuse 4, 0x458B00]
chartreuse: [chartreuse, 0x7FFF00]
chocolate1: [chocolate 1, 0xFF7F24]
chocolate2: [chocolate 2, 0xEE7621]
chocolate3: [chocolate 3, 0xCD661D]
chocolate4: [chocolate 4, 0x8B4513]
chocolate: [chocolate, 0xD2691E]
cobalt: [cobalt, 0x3D59AB]
cobaltgreen: [cobalt green, 0x3D9140]
coldgrey: [cold grey, 0x808A87]
coral1: [coral 1, 0xFF7256]
coral2: [coral 2, 0xEE6A50]
coral3: [coral 3, 0xCD5B45]
coral4: [coral 4, 0x8B3E2F]
coral: [coral, 0xFF7F50]
cornflowerblue: [cornflower blue, 0x6495ED]
cornsilk1: [corn silk 1, 0xFFF8DC]
cornsilk2: [corn silk 2, 0xEEE8CD]
cornsilk3: [corn silk 3, 0xCDC8B1]
cornsilk4: [corn silk 4, 0x8B8878]
cornsilk: [corn silk, 0xFFF8DC]
crimson: [crimson, 0xDC143C]
cyan2: [cyan 2, 0x00EEEE]
cyan3: [cyan 3, 0x00CDCD]
cyan4: [cyan 4, 0x008B8B]
cyan: [cyan, 0x00FFFF]
darkblue: [dark blue, 0x00008B]
darkcyan: [dark cyan, 0x008B8B]
darkgoldenrod1: [dark goldenrod 1, 0xFFB90F]
darkgoldenrod2: [dark goldenrod 2, 0xEEAD0E]
darkgoldenrod3: [dark goldenrod 3, 0xCD950C]
darkgoldenrod4: [dark goldenrod 4, 0x8B6508]
darkgoldenrod: [dark goldenrod, 0xB8860B]
darkgray: [dark gray, 0xA9A9A9]
darkgreen: [dark green, 0x006400]
darkgrey: [dark grey, 0xA9A9A9]
darkkhaki: [dark khaki, 0xBDB76B]
darkmagenta: [dark magenta, 0x8B008B]
darkolivegreen1: [dark olivegreen 1, 0xCAFF70]
darkolivegreen2: [dark olivegreen 2, 0xBCEE68]
darkolivegreen3: [dark olivegreen 3, 0xA2CD5A]
darkolivegreen4: [dark olivegreen 4, 0x6E8B3D]
darkolivegreen: [dark olivegreen, 0x556B2F]
darkorange1: [dark orange 1, 0xFF7F00]
darkorange2: [dark orange 2, 0xEE7600]
darkorange3: [dark orange 3, 0xCD6600]
darkorange4: [dark orange 4, 0x8B4500]
darkorange: [dark orange, 0xFF8C00]
darkorchid1: [dark orchid 1, 0xBF3EFF]
darkorchid2: [dark orchid 2, 0xB23AEE]
darkorchid3: [dark orchid 3, 0x9A32CD]
darkorchid4: [dark orchid 4, 0x68228B]
darkorchid: [dark orchid, 0x9932CC]
darkred: [dark red, 0x8B0000]
darksalmon: [dark salmon, 0xE9967A]
darkseagreen1: [dark sea green 1, 0xC1FFC1]
darkseagreen2: [dark sea green 2, 0xB4EEB4]
darkseagreen3: [dark sea green 3, 0x9BCD9B]
darkseagreen4: [dark sea green 4, 0x698B69]
darkseagreen: [dark sea green, 0x8FBC8F]
darkslateblue: [dark slate blue, 0x483D8B]
darkslategray1: [dark slate gray 1, 0x97FFFF]
darkslategray2: [dark slate gray 2, 0x8DEEEE]
darkslategray3: [dark slate gray 3, 0x79CDCD]
darkslategray4: [dark slate gray 4, 0x528B8B]
darkslategray: [dark slate gray, 0x2F4F4F]
darkslategrey1: [dark slate grey 1, 0x97FFFF]
darkslategrey2: [dark slate grey 2, 0x8DEEEE]
darkslategrey3: [dark slate grey 3, 0x79CDCD]
darkslategrey4: [dark slate grey 4, 0x528B8B]
darkslategrey: [dark slate grey, 0x2F4F4F]
darkturquoise: [dark turquoise, 0x00CED1]
darkviolet: [dark violet, 0x9400D3]
deeppink1: [deep pink 1, 0xFF1493]
deeppink2: [deep pink 2, 0xEE1289]
deeppink3: [deep pink 3, 0xCD1076]
deeppink4: [deep pink 4, 0x8B0A50]
deeppink: [deep pink, 0xFF1493]
deepskyblue1: [deep sky blue 1, 0x00BFFF]
deepskyblue2: [deep sky blue 2, 0x00B2EE]
deepskyblue3: [deep sky blue 3, 0x009ACD]
deepskyblue4: [deep sky blue 4, 0x00688B]
deepskyblue: [deep sky blue, 0x00BFFF]
dimgray: [dim gray, 0x696969]
dimgrey: [dim grey, 0x696969]
dodgerblue1: [dodger blue 1, 0x1E90FF]
dodgerblue2: [dodger blue 2, 0x1C86EE]
dodgerblue3: [dodger blue 3, 0x1874CD]
dodgerblue4: [dodger blue 4, 0x104E8B]
dodgerblue: [dodger blue, 0x1E90FF]
eggshell: [eggshell, 0xFCE6C9]
emeraldgreen: [emerald green, 0x00C957]
firebrick1: [fire brick 1, 0xFF3030]
firebrick2: [fire brick 2, 0xEE2C2C]
firebrick3: [fire brick 3, 0xCD2626]
firebrick4: [fire brick 4, 0x8B1A1A]
firebrick: [fire brick, 0xB22222]
flesh: [flesh, 0xFF7D40]
floralwhite: [floral white, 0xFFFAF0]
forestgreen: [forest green, 0x228B22]
fuchsia: [fuchsia, 0xFF00FF]
gainsboro: [gainsboro, 0xDCDCDC]
ghostwhite: [ghost white, 0xF8F8FF]
gold1: [gold 1, 0xFFD700]
gold2: [gold 2, 0xEEC900]
gold3: [gold 3, 0xCDAD00]
gold4: [gold 4, 0x8B7500]
gold: [gold, 0xFFD700]
goldenrod1: [goldenrod 1, 0xFFC125]
goldenrod2: [goldenrod 2, 0xEEB422]
goldenrod3: [goldenrod 3, 0xCD9B1D]
goldenrod4: [goldenrod 4, 0x8B6914]
goldenrod: [goldenrod, 0xDAA520]
gray10: [gray 10, 0x1A1A1A]
gray11: [gray 11, 0x1C1C1C]
gray12: [gray 12, 0x1F1F1F]
gray13: [gray 13, 0x212121]
gray14: [gray 14, 0x242424]
gray15: [gray 15, 0x262626]
gray16: [gray 16, 0x292929]
gray17: [gray 17, 0x2B2B2B]
gray18: [gray 18, 0x2E2E2E]
gray19: [gray 19, 0x303030]
gray1: [gray 1, 0x030303]
gray20: [gray 20, 0x333333]
gray21: [gray 21, 0x363636]
gray22: [gray 22, 0x383838]
gray23: [gray 23, 0x3B3B3B]
gray24: [gray 24, 0x3D3D3D]
gray25: [gray 25, 0x404040]
gray26: [gray 26, 0x424242]
gray27: [gray 27, 0x454545]
gray28: [gray 28, 0x474747]
gray29: [gray 29, 0x4A4A4A]
gray2: [gray 2, 0x050505]
gray30: [gray 30, 0x4D4D4D]
gray31: [gray 31, 0x4F4F4F]
gray32: [gray 32, 0x525252]
gray33: [gray 33, 0x545454]
gray34: [gray 34, 0x575757]
gray35: [gray 35, 0x595959]
gray36: [gray 36, 0x5C5C5C]
gray37: [gray 37, 0x5E5E5E]
gray38: [gray 38, 0x616161]
gray39: [gray 39, 0x636363]
gray3: [gray 3, 0x080808]
gray40: [gray 40, 0x666666]
gray41: [gray 41, 0x696969]
gray42: [gray 42, 0x6B6B6B]
gray43: [gray 43, 0x6E6E6E]
gray44: [gray 44, 0x707070]
gray45: [gray 45, 0x737373]
gray46: [gray 46, 0x757575]
gray47: [gray 47, 0x787878]
gray48: [gray 48, 0x7A7A7A]
gray49: [gray 49, 0x7D7D7D]
gray4: [gray 4, 0x0A0A0A]
gray50: [gray 50, 0x7F7F7F]
gray51: [gray 51, 0x828282]
gray52: [gray 52, 0x858585]
gray53: [gray 53, 0x878787]
gray54: [gray 54, 0x8A8A8A]
gray55: [gray 55, 0x8C8C8C]
gray56: [gray 56, 0x8F8F8F]
gray57: [gray 57, 0x919191]
gray58: [gray 58, 0x949494]
gray59: [gray 59, 0x969696]
gray5: [gray 5, 0x0D0D0D]
gray60: [gray 60, 0x999999]
gray61: [gray 61, 0x9C9C9C]
gray62: [gray 62, 0x9E9E9E]
gray63: [gray 63, 0xA1A1A1]
gray64: [gray 64, 0xA3A3A3]
gray65: [gray 65, 0xA6A6A6]
gray66: [gray 66, 0xA8A8A8]
gray67: [gray 67, 0xABABAB]
gray68: [gray 68, 0xADADAD]
gray69: [gray 69, 0xB0B0B0]
gray6: [gray 6, 0x0F0F0F]
gray70: [gray 70, 0xB3B3B3]
gray71: [gray 71, 0xB5B5B5]
gray72: [gray 72, 0xB8B8B8]
gray73: [gray 73, 0xBABABA]
gray74: [gray 74, 0xBDBDBD]
gray75: [gray 75, 0xBFBFBF]
gray76: [gray 76, 0xC2C2C2]
gray77: [gray 77, 0xC4C4C4]
gray78: [gray 78, 0xC7C7C7]
gray79: [gray 79, 0xC9C9C9]
gray7: [gray 7, 0x121212]
gray80: [gray 80, 0xCCCCCC]
gray81: [gray 81, 0xCFCFCF]
gray82: [gray 82, 0xD1D1D1]
gray83: [gray 83, 0xD4D4D4]
gray84: [gray 84, 0xD6D6D6]
gray85: [gray 85, 0xD9D9D9]
gray86: [gray 86, 0xDBDBDB]
gray87: [gray 87, 0xDEDEDE]
gray88: [gray 88, 0xE0E0E0]
gray89: [gray 89, 0xE3E3E3]
gray8: [gray 8, 0x141414]
gray90: [gray 90, 0xE5E5E5]
gray91: [gray 91, 0xE8E8E8]
gray92: [gray 92, 0xEBEBEB]
gray93: [gray 93, 0xEDEDED]
gray94: [gray 94, 0xF0F0F0]
gray95: [gray 95, 0xF2F2F2]
gray96: [gray 96, 0xF5F5F5]
gray97: [gray 97, 0xF7F7F7]
gray98: [gray 98, 0xFAFAFA]
gray99: [gray 99, 0xFCFCFC]
gray9: [gray 9, 0x171717]
gray: [gray, 0x808080]
green1: [green 1, 0x00FF00]
green2: [green 2, 0x00EE00]
green3: [green 3, 0x00CD00]
green4: [green 4, 0x008B00]
green: [green, 0x00FF00]
greenyellow: [green yellow, 0xADFF2F]
grey10: [grey 10, 0x1A1A1A]
grey11: [grey 11, 0x1C1C1C]
grey12: [grey 12, 0x1F1F1F]
grey13: [grey 13, 0x212121]
grey14: [grey 14, 0x242424]
grey15: [grey 15, 0x262626]
grey16: [grey 16, 0x292929]
grey17: [grey 17, 0x2B2B2B]
grey18: [grey 18, 0x2E2E2E]
grey19: [grey 19, 0x303030]
grey1: [grey 1, 0x030303]
grey20: [grey 20, 0x333333]
grey21: [grey 21, 0x363636]
grey22: [grey 22, 0x383838]
grey23: [grey 23, 0x3B3B3B]
grey24: [grey 24, 0x3D3D3D]
grey25: [grey 25, 0x404040]
grey26: [grey 26, 0x424242]
grey27: [grey 27, 0x454545]
grey28: [grey 28, 0x474747]
grey29: [grey 29, 0x4A4A4A]
grey2: [grey 2, 0x050505]
grey30: [grey 30, 0x4D4D4D]
grey31: [grey 31, 0x4F4F4F]
grey32: [grey 32, 0x525252]
grey33: [grey 33, 0x545454]
grey34: [grey 34, 0x575757]
grey35: [grey 35, 0x595959]
grey36: [grey 36, 0x5C5C5C]
grey37: [grey 37, 0x5E5E5E]
grey38: [grey 38, 0x616161]
grey39: [grey 39, 0x636363]
grey3: [grey 3, 0x080808]
grey40: [grey 40, 0x666666]
grey41: [grey 41, 0x696969]
grey42: [grey 42, 0x6B6B6B]
grey43: [grey 43, 0x6E6E6E]
grey44: [grey 44, 0x707070]
grey45: [grey 45, 0x737373]
grey46: [grey 46, 0x757575]
grey47: [grey 47, 0x787878]
grey48: [grey 48, 0x7A7A7A]
grey49: [grey 49, 0x7D7D7D]
grey4: [grey 4, 0x0A0A0A]
grey50: [grey 50, 0x7F7F7F]
grey51: [grey 51, 0x828282]
grey52: [grey 52, 0x858585]
grey53: [grey 53, 0x878787]
grey54: [grey 54, 0x8A8A8A]
grey55: [grey 55, 0x8C8C8C]
grey56: [grey 56, 0x8F8F8F]
grey57: [grey 57, 0x919191]
grey58: [grey 58, 0x949494]
grey59: [grey 59, 0x969696]
grey5: [grey 5, 0x0D0D0D]
grey60: [grey 60, 0x999999]
grey61: [grey 61, 0x9C9C9C]
grey62: [grey 62, 0x9E9E9E]
grey63: [grey 63, 0xA1A1A1]
grey64: [grey 64, 0xA3A3A3]
grey65: [grey 65, 0xA6A6A6]
grey66: [grey 66, 0xA8A8A8]
grey67: [grey 67, 0xABABAB]
grey68: [grey 68, 0xADADAD]
grey69: [grey 69, 0xB0B0B0]
grey6: [grey 6, 0x0F0F0F]
grey70: [grey 70, 0xB3B3B3]
grey71: [grey 71, 0xB5B5B5]
grey72: [grey 72, 0xB8B8B8]
grey73: [grey 73, 0xBABABA]
grey74: [grey 74, 0xBDBDBD]
grey75: [grey 75, 0xBFBFBF]
grey76: [grey 76, 0xC2C2C2]
grey77: [grey 77, 0xC4C4C4]
grey78: [grey 78, 0xC7C7C7]
grey79: [grey 79, 0xC9C9C9]
grey7: [grey 7, 0x121212]
grey80: [grey 80, 0xCCCCCC]
grey81: [grey 81, 0xCFCFCF]
grey82: [grey 82, 0xD1D1D1]
grey83: [grey 83, 0xD4D4D4]
grey84: [grey 84, 0xD6D6D6]
grey85: [grey 85, 0xD9D9D9]
grey86: [grey 86, 0xDBDBDB]
grey87: [grey 87, 0xDEDEDE]
grey88: [grey 88, 0xE0E0E0]
grey89: [grey 89, 0xE3E3E3]
grey8: [grey 8, 0x141414]
grey90: [grey 90, 0xE5E5E5]
grey91: [grey 91, 0xE8E8E8]
grey92: [grey 92, 0xEBEBEB]
grey93: [grey 93, 0xEDEDED]
grey94: [grey 94, 0xF0F0F0]
grey95: [grey 95, 0xF2F2F2]
grey96: [grey 96, 0xF5F5F5]
grey97: [grey 97, 0xF7F7F7]
grey98: [grey 98, 0xFAFAFA]
grey99: [grey 99, 0xFCFCFC]
grey9: [grey 9, 0x171717]
grey: [grey, 0x808080]
honeydew1: [honeydew 1, 0xF0FFF0]
honeydew2: [honeydew 2, 0xE0EEE0]
honeydew3: [honeydew 3, 0xC1CDC1]
honeydew4: [honeydew 4, 0x838B83]
honeydew: [honeydew, 0xF0FFF0]
hotpink1: [hot pink 1, 0xFF6EB4]
hotpink2: [hot pink 2, 0xEE6AA7]
hotpink3: [hot pink 3, 0xCD6090]
hotpink4: [hot pink 4, 0x8B3A62]
hotpink: [hot pink, 0xFF69B4]
indianred1: [indian red 1, 0xFF6A6A]
indianred2: [indian red 2, 0xEE6363]
indianred3: [indian red 3, 0xCD5555]
indianred4: [indian red 4, 0x8B3A3A]
indianred: [indian red, 0xC05C5C]
indigo: [indigo, 0x4B0082]
ivory1: [ivory 1, 0xFFFFF0]
ivory2: [ivory 2, 0xEEEEE0]
ivory3: [ivory 3, 0xCDCDC1]
ivory4: [ivory 4, 0x8B8B83]
ivory: [ivory, 0xFFFFF0]
ivoryblack: [ivory black, 0x292421]
khaki1: [khaki 1, 0xFFF68F]
khaki2: [khaki 2, 0xEEE685]
khaki3: [khaki 3, 0xCDC673]
khaki4: [khaki 4, 0x8B864E]
khaki: [khaki, 0xF0E68C]
lavender: [lavender, 0xE6E6FA]
lavenderblush1: [lavender blush 1, 0xFFF0F5]
lavenderblush2: [lavender blush 2, 0xEEE0E5]
lavenderblush3: [lavender blush 3, 0xCDC1C5]
lavenderblush4: [lavender blush 4, 0x8B8386]
lavenderblush: [lavender blush, 0xFFF0F5]
lawngreen: [lawn green, 0x7CFC00]
lemonchiffon1: [lemon chiffon 1, 0xFFFACD]
lemonchiffon2: [lemon chiffon 2, 0xEEE9BF]
lemonchiffon3: [lemon chiffon 3, 0xCDC9A5]
lemonchiffon4: [lemon chiffon 4, 0x8B8970]
lemonchiffon: [lemon chiffon, 0xFFFACD]
lightblue1: [light blue 1, 0xBFEFFF]
lightblue2: [light blue 2, 0xB2DFEE]
lightblue3: [light blue 3, 0x9AC0CD]
lightblue4: [light blue 4, 0x68838B]
lightblue: [light blue, 0xADD8E6]
lightcoral: [light coral, 0xF08080]
lightcyan1: [light cyan 1, 0xE0FFFF]
lightcyan2: [light cyan 2, 0xD1EEEE]
lightcyan3: [light cyan 3, 0xB4CDCD]
lightcyan4: [light cyan 4, 0x7A8B8B]
lightcyan: [light cyan, 0xE0FFFF]
lightgoldenrod1: [light goldenrod 1, 0xFFEC8B]
lightgoldenrod2: [light goldenrod 2, 0xEEDC82]
lightgoldenrod3: [light goldenrod 3, 0xCDBE70]
lightgoldenrod4: [light goldenrod 4, 0x8B814C]
lightgoldenrodyellow: [light goldenrod yellow, 0xFAFAD2]
lightgreen: [light green, 0x90EE90]
lightgrey: [light grey, 0xD3D3D3]
lightpink1: [light pink 1, 0xFFAEB9]
lightpink2: [light pink 2, 0xEEA2AD]
lightpink3: [light pink 3, 0xCD8C95]
lightpink4: [light pink 4, 0x8B5F65]
lightpink: [light pink, 0xFFB6C1]
lightsalmon1: [light salmon 1, 0xFFA07A]
lightsalmon2: [light salmon 2, 0xEE9572]
lightsalmon3: [light salmon 3, 0xCD8162]
lightsalmon4: [light salmon 4, 0x8B5742]
lightsalmon: [light salmon, 0xFFA07A]
lightseagreen: [light sea green, 0x20B2AA]
lightskyblue1: [light sky blue 1, 0xB0E2FF]
lightskyblue2: [light sky blue 2, 0xA4D3EE]
lightskyblue3: [light sky blue 3, 0x8DB6CD]
lightskyblue4: [light sky blue 4, 0x607B8B]
lightskyblue: [light sky blue, 0x87CEFA]
lightslateblue: [light slate blue, 0x8470FF]
lightslategray: [light slate gray, 0x778899]
lightslategrey: [light slate grey, 0x778899]
lightsteelblue1: [light steel blue 1, 0xCAE1FF]
lightsteelblue2: [light steel blue 2, 0xBCD2EE]
lightsteelblue3: [light steel blue 3, 0xA2B5CD]
lightsteelblue4: [light steel blue 4, 0x6E7B8B]
lightsteelblue: [light steel blue, 0xB0C4DE]
lightyellow1: [light yellow 1, 0xFFFFE0]
lightyellow2: [light yellow 2, 0xEEEED1]
lightyellow3: [light yellow 3, 0xCDCDB4]
lightyellow4: [light yellow 4, 0x8B8B7A]
lightyellow: [light yellow, 0xFFFFE0]
lime: [lime, 0x00FF00]
limegreen: [lime green, 0x32CD32]
linen: [linen, 0xFAF0E6]
magenta2: [magenta 2, 0xEE00EE]
magenta3: [magenta 3, 0xCD00CD]
magenta4: [magenta 4, 0x8B008B]
magenta: [magenta, 0xFF00FF]
manganeseblue: [manganese blue, 0x03A89E]
maroon1: [maroon 1, 0xFF34B3]
maroon2: [maroon 2, 0xEE30A7]
maroon3: [maroon 3, 0xCD2990]
maroon4: [maroon 4, 0x8B1C62]
maroon: [maroon, 0x800000]
mediumaquamarine: [medium aquamarine, 0x66CDAA]
mediumblue: [medium blue, 0x0000CD]
mediumorchid1: [medium orchid 1, 0xE066FF]
mediumorchid2: [medium orchid 2, 0xD15FEE]
mediumorchid3: [medium orchid 3, 0xB452CD]
mediumorchid4: [medium orchid 4, 0x7A378B]
mediumorchid: [medium orchid, 0xBA55D3]
mediumpurple1: [medium purple 1, 0xAB82FF]
mediumpurple2: [medium purple 2, 0x9F79EE]
mediumpurple3: [medium purple 3, 0x8968CD]
mediumpurple4: [medium purple 4, 0x5D478B]
mediumpurple: [medium purple, 0x9370DB]
mediumseagreen: [medium sea green, 0x3CB371]
mediumslateblue: [medium slate blue, 0x7B68EE]
mediumspringgreen: [medium spring green, 0x00FA9A]
mediumturquoise: [medium turquoise, 0x48D1CC]
mediumvioletred: [medium violetred, 0xC71585]
melon: [melon, 0xE3A869]
midnightblue: [midnight blue, 0x191970]
mint: [mint, 0xBDFCC9]
mintcream: [mint cream, 0xF5FFFA]
mistyrose1: [misty rose 1, 0xFFE4E1]
mistyrose2: [misty rose 2, 0xEED5D2]
mistyrose3: [misty rose 3, 0xCDB7B5]
mistyrose4: [misty rose 4, 0x8B7D7B]
mistyrose: [misty rose, 0xFFE4E1]
moccasin: [moccasin, 0xFFE4B5]
navajowhite1: [navajo white 1, 0xFFDEAD]
navajowhite2: [navajo white 2, 0xEECFA1]
navajowhite3: [navajo white 3, 0xCDB38B]
navajowhite4: [navajo white 4, 0x8B795E]
navajowhite: [navajo white, 0xFFDEAD]
navy: [navy, 0x000080]
oldlace: [old lace, 0xFDF5E6]
olive: [olive, 0x808000]
olivedrab1: [olive drab 1, 0xC0FF3E]
olivedrab2: [olive drab 2, 0xB3EE3A]
olivedrab3: [olive drab 3, 0x9ACD32]
olivedrab4: [olive drab 4, 0x698B22]
olivedrab: [olive drab, 0x6B8E23]
orange1: [orange 1, 0xFFA500]
orange2: [orange 2, 0xEE9A00]
orange3: [orange 3, 0xCD8500]
orange4: [orange 4, 0x8B5A00]
orange: [orange, 0xFF8000]
orangered1: [orange red 1, 0xFF4500]
orangered2: [orange red 2, 0xEE4000]
orangered3: [orange red 3, 0xCD3700]
orangered4: [orange red 4, 0x8B2500]
orangered: [orange red, 0xFF4500]
orchid1: [orchid 1, 0xFF83FA]
orchid2: [orchid 2, 0xEE7AE9]
orchid3: [orchid 3, 0xCD69C9]
orchid4: [orchid 4, 0x8B4789]
orchid: [orchid, 0xDA70D6]
palegoldenrod: [pale goldenrod, 0xEEE8AA]
palegreen1: [pale green 1, 0x9AFF9A]
palegreen2: [pale green 2, 0x90EE90]
palegreen3: [pale green 3, 0x7CCD7C]
palegreen4: [pale green 4, 0x548B54]
palegreen: [pale green, 0x98FB98]
paleturquoise1: [pale turquoise 1, 0xBBFFFF]
paleturquoise2: [pale turquoise 2, 0xAEEEEE]
paleturquoise3: [pale turquoise 3, 0x96CDCD]
paleturquoise4: [pale turquoise 4, 0x668B8B]
paleturquoise: [pale turquoise, 0xAEEEEE]
palevioletred1: [pale violet red 1, 0xFF82AB]
palevioletred2: [pale violet red 2, 0xEE799F]
palevioletred3: [pale violet red 3, 0xCD6889]
palevioletred4: [pale violet red 4, 0x8B475D]
palevioletred: [pale violet red, 0xDB7093]
papayawhip: [papaya whip, 0xFFEFD5]
peachpuff1: [peachpuff 1, 0xFFDAB9]
peachpuff2: [peachpuff 2, 0xEECBAD]
peachpuff3: [peachpuff 3, 0xCDAF95]
peachpuff4: [peachpuff 4, 0x8B7765]
peachpuff: [peachpuff, 0xFFDAB9]
peacock: [peacock, 0x33A1C9]
peru: [peru, 0xCD853F]
pink1: [pink 1, 0xFFB5C5]
pink2: [pink 2, 0xEEA9B8]
pink3: [pink 3, 0xCD919E]
pink4: [pink 4, 0x8B636C]
pink: [pink, 0xFFC0CB]
plum1: [plum 1, 0xFFBBFF]
plum2: [plum 2, 0xEEAEEE]
plum3: [plum 3, 0xCD96CD]
plum4: [plum 4, 0x8B668B]
plum: [plum, 0xDDA0DD]
powderblue: [powder blue, 0xB0E0E6]
purple1: [purple 1, 0x9B30FF]
purple2: [purple 2, 0x912CEE]
purple3: [purple 3, 0x7D26CD]
purple4: [purple 4, 0x551A8B]
purple: [purple, 0x800080]
raspberry: [raspberry, 0x872657]
rawsienna: [raw sienna, 0xC76114]
red1: [red 1, 0xFF0000]
red2: [red 2, 0xEE0000]
red3: [red 3, 0xCD0000]
red4: [red 4, 0x8B0000]
red: [red, 0xFF0000]
rosybrown1: [rosy brown 1, 0xFFC1C1]
rosybrown2: [rosy brown 2, 0xEEB4B4]
rosybrown3: [rosy brown 3, 0xCD9B9B]
rosybrown4: [rosy brown 4, 0x8B6969]
rosybrown: [rosy brown, 0xBC8F8F]
royalblue1: [royal blue 1, 0x4876FF]
royalblue2: [royal blue 2, 0x436EEE]
royalblue3: [royal blue 3, 0x3A5FCD]
royalblue4: [royal blue 4, 0x27408B]
royalblue: [royal blue, 0x4169E1]
saddlebrown: [saddle brown, 0x8B4513]
salmon1: [salmon 1, 0xFF8C69]
salmon2: [salmon 2, 0xEE8262]
salmon3: [salmon 3, 0xCD7054]
salmon4: [salmon 4, 0x8B4C39]
salmon: [salmon, 0xFA8072]
sandybrown: [sandy brown, 0xF4A460]
sapgreen: [sap green, 0x308014]
seagreen1: [sea green 1, 0x54FF9F]
seagreen2: [sea green 2, 0x4EEE94]
seagreen3: [sea green 3, 0x43CD80]
seagreen4: [sea green 4, 0x2E8B57]
seagreen: [sea green, 0x2E8B57]
seashell1: [seashell 1, 0xFFF5EE]
seashell2: [seashell 2, 0xEEE5DE]
seashell3: [seashell 3, 0xCDC5BF]
seashell4: [seashell 4, 0x8B8682]
seashell: [seashell, 0xFFF5EE]
sepia: [sepia, 0x5E2612]
sgibeet: [sgi beet, 0x8E388E]
sgibrightgray: [sgi bright gray, 0xC5C1AA]
sgibrightgrey: [sgi bright grey, 0xC5C1AA]
sgichartreuse: [sgi chartreuse, 0x71C671]
sgidarkgray: [sgi dark gray, 0x555555]
sgidarkgrey: [sgi dark grey, 0x555555]
sgigray12: [sgi gray 12, 0x1E1E1E]
sgigray16: [sgi gray 16, 0x282828]
sgigray32: [sgi gray 32, 0x515151]
sgigray36: [sgi gray 36, 0x5B5B5B]
sgigray52: [sgi gray 52, 0x848484]
sgigray56: [sgi gray 56, 0x8E8E8E]
sgigray72: [sgi gray 72, 0xB7B7B7]
sgigray76: [sgi gray 76, 0xC1C1C1]
sgigray92: [sgi gray 92, 0xEAEAEA]
sgigray96: [sgi gray 96, 0xF4F4F4]
sgigrey12: [sgi grey 12, 0x1E1E1E]
sgigrey16: [sgi grey 16, 0x282828]
sgigrey32: [sgi grey 32, 0x515151]
sgigrey36: [sgi grey 36, 0x5B5B5B]
sgigrey52: [sgi grey 52, 0x848484]
sgigrey56: [sgi grey 56, 0x8E8E8E]
sgigrey72: [sgi grey 72, 0xB7B7B7]
sgigrey76: [sgi grey 76, 0xC1C1C1]
sgigrey92: [sgi grey 92, 0xEAEAEA]
sgigrey96: [sgi grey 96, 0xF4F4F4]
sgilightblue: [sgi light blue, 0x7D9EC0]
sgilightgray: [sgi light gray, 0xAAAAAA]
sgilightgrey: [sgi light grey, 0xAAAAAA]
sgiolivedrab: [sgi olive drab, 0x8E8E38]
sgisalmon: [sgi salmon, 0xC67171]
sgislateblue: [sgi slateblue, 0x7171C6]
sgiteal: [sgi teal, 0x388E8E]
sienna1: [sienna 1, 0xFF8247]
sienna2: [sienna 2, 0xEE7942]
sienna3: [sienna 3, 0xCD6839]
sienna4: [sienna 4, 0x8B4726]
sienna: [sienna, 0xA0522D]
silver: [silver, 0xC0C0C0]
skyblue1: [sky blue 1, 0x87CEFF]
skyblue2: [sky blue 2, 0x7EC0EE]
skyblue3: [sky blue 3, 0x6CA6CD]
skyblue4: [sky blue 4, 0x4A708B]
skyblue: [sky blue, 0x87CEEB]
slateblue1: [slate blue 1, 0x836FFF]
slateblue2: [slate blue 2, 0x7A67EE]
slateblue3: [slate blue 3, 0x6959CD]
slateblue4: [slate blue 4, 0x473C8B]
slateblue: [slate blue, 0x6A5ACD]
slategray1: [slate gray 1, 0xC6E2FF]
slategray2: [slate gray 2, 0xB9D3EE]
slategray3: [slate gray 3, 0x9FB6CD]
slategray4: [slate gray 4, 0x6C7B8B]
slategray: [slate gray, 0x708090]
slategrey1: [slate grey 1, 0xC6E2FF]
slategrey2: [slate grey 2, 0xB9D3EE]
slategrey3: [slate grey 3, 0x9FB6CD]
slategrey4: [slate grey 4, 0x6C7B8B]
slategrey: [slate grey, 0x708090]
snow1: [snow 1, 0xFFFAFA]
snow2: [snow 2, 0xEEE9E9]
snow3: [snow 3, 0xCDC9C9]
snow4: [snow 4, 0x8B8989]
snow: [snow, 0xFFFAFA]
springgreen1: [spring green 1, 0x00EE76]
springgreen2: [spring green 2, 0x00CD66]
springgreen3: [spring green 3, 0x008B45]
springgreen: [spring green, 0x00FF7F]
steelblue1: [steel blue 1, 0x63B8FF]
steelblue2: [steel blue 2, 0x5CACEE]
steelblue3: [steel blue 3, 0x4F94CD]
steelblue4: [steel blue 4, 0x36648B]
steelblue: [steel blue, 0x4682B4]
tan1: [tan 1, 0xFFA54F]
tan2: [tan 2, 0xEE9A49]
tan3: [tan 3, 0xCD853F]
tan4: [tan 4, 0x8B5A2B]
tan: [tan, 0xD2B48C]
teal: [teal, 0x008080]
thistle1: [thistle 1, 0xFFE1FF]
thistle2: [thistle 2, 0xEED2EE]
thistle3: [thistle 3, 0xCDB5CD]
thistle4: [thistle 4, 0x8B7B8B]
thistle: [thistle, 0xD8BFD8]
tomato1: [tomato 1, 0xFF6347]
tomato2: [tomato 2, 0xEE5C42]
tomato3: [tomato 3, 0xCD4F39]
tomato4: [tomato 4, 0x8B3626]
tomato: [tomato, 0xFF6347]
turquoise1: [turquoise 1, 0x00F5FF]
turquoise2: [turquoise 2, 0x00E5EE]
turquoise3: [turquoise 3, 0x00C5CD]
turquoise4: [turquoise 4, 0x00868B]
turquoise: [turquoise, 0x40E0D0]
turquoiseblue: [turquoise blue, 0x00C78C]
violet: [violet, 0xEE82EE]
violetred1: [violet red 1, 0xFF3E96]
violetred2: [violet red 2, 0xEE3A8C]
violetred3: [violet red 3, 0xCD3278]
violetred4: [violet red 4, 0x8B2252]
violetred: [violet red, 0xD02090]
warmgrey: [warm grey, 0x808069]
wheat1: [wheat 1, 0xFFE7BA]
wheat2: [wheat 2, 0xEED8AE]
wheat3: [wheat 3, 0xCDBA96]
wheat4: [wheat 4, 0x8B7E66]
wheat: [wheat, 0xF5DEB3]
white: [white, 0xFFFFFF]
whitesmoke: [white smoke, 0xF5F5F5]
yellow1: [yellow 1, 0xFFFF00]
yellow2: [yellow 2, 0xEEEE00]
yellow3: [yellow 3, 0xCDCD00]
yellow4: [yellow 4, 0x8B8B00]
yellow: [yellow, 0xFFFF00]
yellowgreen: [yellow green, 0x9ACD32]
""")
