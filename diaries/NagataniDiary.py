from diaries.AbstractDiary import AbstractDiary

class NagataniDiary(AbstractDiary):
  def get_date(self):
    return "2022-12-15"

  def get_summary(self):
    return "課題を何とか出し終えた。レポートの内容多すぎて、つらかった。"

  def get_author(self):
    return "ながたに"