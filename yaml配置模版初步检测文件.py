import tkinter as tk
from tkinter import ttk
import yaml

yaml_definitions = {
    "instance_type": "实例类型",
    "image_id": "镜像ID",
    "security_group_ids": "安全组ID列表",
    "subnet_id": "子网ID",
    "key_name": "SSH密钥名称",
    "tags": "标签（键-值对）",
    "script_path": "脚本路径",
    "access_key": "Access Key",
    "secret_key": "Secret Key"
}

yaml_examples = {
    "instance_type": "instance_type: t3.micro",
    "image_id": "image_id: ami-12345678",
    "security_group_ids": "security_group_ids:\n  - sg-abcdefg\n  - sg-hijklmn",
    "subnet_id": "subnet_id: subnet-12345678",
    "key_name": "key_name: my-key-pair",
    "tags": "tags:\n  Name: MyInstance\n  Environment: Production",
    "script_path": "script_path: /path/to/script.sh",
    "access_key": "access_key: YOUR_ACCESS_KEY",
    "secret_key": "secret_key: YOUR_SECRET_KEY"
}


def on_yaml_definition_selected(event):
    # 获取选中的YAML定义
    selected_item = yaml_listbox.get(yaml_listbox.curselection())
    # 获取对应的中文提示和示例
    hint = yaml_definitions[selected_item]
    example = yaml_examples[selected_item]
    # 在文本框中插入选中的YAML定义、中文提示和示例
    yaml_text.insert(tk.END, "{}:  # {}\n{}\n\n".format(selected_item, hint, example))


def generate_template():
    # 获取文本框中的YAML代码
    yaml_code = yaml_text.get("1.0", tk.END)
    try:
        # 解析YAML代码并转换为Python对象
        yaml_obj = yaml.safe_load(yaml_code)

        # 检查AK/SK是否存在
        if "access_key" in yaml_obj and "secret_key" in yaml_obj:
            access_key = yaml_obj["access_key"]
            secret_key = yaml_obj["secret_key"]
            if access_key == "" or secret_key == "":
                raise ValueError("Access Key和Secret Key不能为空")

        # 生成YAML模板
        template = yaml.dump(yaml_obj, default_flow_style=False)
        # 显示生成的模板
        result_label.config(text=template, fg="green")
        # 将模板写入目标文件
        with open("target.yaml", "w") as f:
            f.write(template)
        # 显示输出目标文件的消息
        output_label.config(text="模板已成功输出到 target.yaml 文件中", fg="blue")
    except Exception as e:
        # 如果解析出错，显示错误信息
        result_label.config(text=str(e), fg="red")


root = tk.Tk()
root.title("YAML模板生成器")

# 创建YAML定义列表框
yaml_listbox = tk.Listbox(root)
yaml_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# 将示例YAML定义添加到列表框中
for definition, hint in yaml_definitions.items():
    yaml_listbox.insert(tk.END, definition)

# 创建滚动条
scrollbar = ttk.Scrollbar(root, command=yaml_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
yaml_listbox.config(yscrollcommand=scrollbar.set)

# 创建文本框
yaml_text = tk.Text(root, height=10, width=50)
yaml_text.pack()

# 创建生成模板按钮
generate_button = tk.Button(root, text="生成模板", command=generate_template)
generate_button.pack()

# 创建结果标签
result_label = tk.Label(root, text="", fg="black")
result_label.pack()

# 创建输出目标文件的标签
output_label = tk.Label(root, text="", fg="black")
output_label.pack()

# 绑定选择事件
yaml_listbox.bind("<<ListboxSelect>>", on_yaml_definition_selected)

root.mainloop()
