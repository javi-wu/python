import random

answer = random.randint(1,100)
count = 0
max_attempts = 7

print("欢迎来到猜数字游戏！你有7次机会猜1-100之间的数字。")

while count < max_attempts:
    try:
        guess = int(input(f"第{count + 1}次猜测，请输入数字: "))
    except ValueError:
        print("请输入有效的整数！")
        continue  # 无效输入不计次数

    count += 1  # 只有有效猜测才计数

    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print(f"🎉 恭喜！你猜中了！答案是 {answer}，用了 {count} 次。")
        break
else:
    # while 循环正常结束（即猜了7次都没中）
    print(f"😢 游戏结束！你已用完{max_attempts}次机会。正确答案是: {answer}")