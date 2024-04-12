# Pandas: Remove special characters from Column Values

import pandas as pd

df = pd.DataFrame({
    '$name$': ['Ali#ce', 'Bobby@', 'Ca$r%l', 'D^a&n'],
    '!experience@': [11, 14, 16, 18],
    '^salary*': [175.1, 180.2, 190.3, 210.4],
})

df['$name$'] = df['$name$'].str.replace(r'\W', '', regex=True)

#   $name$  !experience@  ^salary*
# 0  Alice            11     175.1
# 1  Bobby            14     180.2
# 2   Carl            16     190.3
# 3    Dan            18     210.4
print(df)