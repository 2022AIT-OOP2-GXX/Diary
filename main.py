from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
  DiarySample(),
  NagataniDiary(),
  NagataniDiary(),
  NagataniDiary(),
]

for d in diaries:
  print("---------------------------------")
  print(d.get_date())
  print(d.get_summary())
  print(d.get_author())
  print()