    cannon_html = f"""
    <style>
    .cannon-wrapper {{
        position: relative;
        text-align: center;
        margin-top: 50px;
        height: 300px;  /* 이 부분도 여유 있게 */
        overflow: visible;
    }}
    .cannon {{
        width: 120px;
        margin-top: 100px;
    }}
    .food-shot {{
        font-size: 30px;
        font-weight: bold;
        color: #FF5722;
        position: absolute;
        left: 50%;
        top: 70px;
        transform: translateX(-50%);
        opacity: 0;
        animation: shoot 1.3s ease-out forwards;
    }}
    @keyframes shoot {{
        0% {{
            opacity: 0;
            transform: translateX(-50%) translateY(0px) scale(0.3);
        }}
        50% {{
            opacity: 1;
            transform: translateX(-50%) translateY(-60px) scale(1.3);
        }}
        100% {{
            transform: translateX(-50%) translateY(-180px) scale(1);
            opacity: 1;
        }}
    }}
    </style>

    <div class="cannon-wrapper">
        <div class="food-shot">{chosen_food} <span style='font-size:16px;'>({chosen_category})</span></div>
        <img class="cannon" src="https://cdn-icons-png.flaticon.com/512/727/727399.png" />
    </div>
    """

    components.html(cannon_html, height=500)  # 👉 여기! 500으로 충분히 공간 확보

