from datetime import datetime

class Task():
    def __init__(self, task_desc: str, task_creation: datetime, task_deadline: datetime, is_done: bool):
        self.task_desc = task_desc
        self.task_creation = task_creation
        self.task_deadline = task_deadline
        self.is_done = is_done
        self.conclusion_date = None

    def conclude_task(self) -> None:
        self.is_done = True
        self.conclusion_date = datetime.now()
    
    def is_past_deadline(self) -> bool:
        return not self.is_done and datetime.now() > self.task_deadline

    def __str__(self) -> str:
        return f"""
            DESCRIÇÃO: {self.task_desc}DATA DE CRIAÇÃO: {self.task_creation}
            TEMPO LIMITE: {self.task_deadline}
            ESTÁ CONCLUIDA: {"não" if not self.is_done else "sim"}
            QUANDO CONCLUIDA: {"<não concluido>" if self.is_past_deadline() else self.conclusion_date}
        """