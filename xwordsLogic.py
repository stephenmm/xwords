#!/usr/bin/python3
import re, pprint, random
pp = pprint.PrettyPrinter(indent=2)

class Cons:
    STD_ENG_TILE_COUNT = 100
    STD_ENG_SCRBL_DIST = { '_'=2, 'a'=9, 'b'=2, 'c'=2, 'd'=4, 'e'=12,'f'=2, 'g'=3, 'h'=2, 'i'=9, 'j'=1, 'k'=1, 'l'=4, 'm'=2, 'n'=6, 'o'=8, 'p'=2, 'q'=1 , 'r'=6, 's'=4, 't'=6, 'u'=4, 'v'=2, 'w'=2, 'x'=1, 'y'=2, 'z'=1  }
    STD_ENG_SCRBL_VALS = { '_'=0, 'a'=1, 'b'=3, 'c'=3, 'd'=2, 'e'=1, 'f'=4, 'g'=2, 'h'=4, 'i'=1, 'j'=8, 'k'=5, 'l'=1, 'm'=3, 'n'=1, 'o'=1, 'p'=3, 'q'=10, 'r'=1, 's'=1, 't'=1, 'u'=1, 'v'=4, 'w'=4, 'x'=8, 'y'=4, 'z'=10 }

    TILE_COUNT=STD_ENG_TILE_COUNT
    DIST=STD_ENG_SCRBL_DIST
    VALS=STD_ENG_SCRBL_VALS


class Tiles():
  def __init__(self,id,ltr,val):
    self.id=id
    self.ltr=ltr.lower()
    self.val=val
    self.loc=-1
    self.n=0
    self.w=0
    self.s=0
    self.e=0

class Player():
  def __init__(self,name=""):
    self.points=0
    self.tiles=[];
    if name=="":
      self.ltr=self.askForName()
  def addPoints(pts):
    self.points+=pts
  def addTiles(tiles=[]):
    self.tiles.append( tiles )
      if( len( self.tiles ) > 7 ):
        raise SystemError("The player %s has to many tiles %d"%(self.ltr,len(self.tiles)))
  def AskForName():


class XwordsLogic():
  def __init__(self):
    self.bag=[]
    self.plyrs=[]
    cnt=0
    for ltr num in Cons.DIST:
      for i in num:
        self.bag.append( Tiles(cnt, ltr, Cons.VALS[ltr]) )
        cnt+=1
    if( len( self.bag ) > Cons.TILE_COUNT ):
      raise SystemError("The bag has too many tiles %d"%(len(self.bag)))
    random.shuffle( self.bag )
    nPlyrs=self.getNumberPlayers()
    for n in nPlyrs:
      self.plyrs.append( Player( "plyr%d"%n ) ) # TODO - leave empty to add real names
    firstPlyr=1 # TODO - First player based on random bag pick whoever got lowest value
    turn=0



  def getNumberPlayers( N ):
    print( "getNumberPlayers: TODO- for no just return 4")
    return 4;

  def getNBagTiles( N ):
    rtrn=[]
    for n in N:
      i=random.randint(0,len(self.bag)-1)
      rtrn.append( self.bag.pop(i) )
  return rtrn

  def chkBrd(): print("TODO");

  def MainGameLoop():
    for p in player:
      self.getNextWord( plyrs[

rckLtrs = 'kduemsp'
brdTiles = [
  {'ltr':'p', 'loc':183, 'n':2,  'w':3,  's':4,  'e':1 },
  {'ltr':'q', 'loc':186, 'n':2,  'w':1,  's':12, 'e':9 },
  {'ltr':'d', 'loc':125, 'n':6,  'w':5,  's':8,  'e':9 },
  {'ltr':'d', 'loc':93,  'n':4,  'w':3,  's':6,  'e':11}
]
brdLtrs = ''
for brdTile in brdTiles:
  if brdTile['loc'] >= 0:
    brdLtrs+=brdTile['ltr']
pp.pprint( brdLtrs )

f = open('scrable_dictionary.txt')
contents = f.read()
file_as_list = contents.splitlines()

vldRckWrds=[]

# Find all the words player can make from the tiles in her rack
for line in file_as_list:
  #print('.', end='')
  m = re.search( r'^([%s]{0,7})([%s])([%s]{0,7})$'%(rckLtrs, brdLtrs, rckLtrs), line, re.IGNORECASE )
  if m:
    match = m[1]+m[2]+m[3]
    print(match, end=' '),
    # Save vldMatch where each rckTile is only used once
    for l in rckLtrs.upper():
      match=match.replace( l, '', 1 )
    if len( match ) <= 1:
      vldRckWrds.append( {
                           'word':m[1].lower()+m[2].upper()+m[3].lower(),
                           'leadLen':len(m[1]),
                           'trailLen':len(m[3]),
                           'brdLtr':m[2]
                         } )

pp.pprint( vldRckWrds )
print( "len(vldRckWrds):%s"% len(vldRckWrds))

vldBrdWrds=[]
# Find where it can be placed on the board
for vldRckWrd in vldRckWrds:
  brdLtrMatchs = [tile for tile in brdTiles if tile['ltr']==vldRckWrd['brdLtr'] ]
  brdWrdFits = [tile for tile in brdLtrMatchs if (( tile['n']>=leadLen and tile['s']>=tailLen ) or ( tile['w']>=leadLen and tile['e']>=tailLen )) ]
  print( "%s" % vldRckWrd['word'], end=' ' )
  #pp.pprint( brdWrdFits )
  #vldBrdWrds.append( {

print( "len(vldRckWrds):%s"% len(vldRckWrds))


def main():
    root = tk.Tk()
    nib = Xwords()
    root.mainloop()

if __ltr__ == '__main__':
    main()
