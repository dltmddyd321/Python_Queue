#연결리스트를 이용한 큐(FIFO) 구현

class Node :
    def __init__(self):
        self.data = None
        self.link = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def printQueue(self):
        if self.front == None:
            print("데이터가 없습니다")

        else:
            current = self.front #큐의 첫 노드를 현재값에 준다.
            while current != None: #마지막 노드까지 반복
                print(current.data)#현재노드의 데이터값 출력
                current = current.link #다음 노드로 이동
            print()

    def enQueue(self, newData):
        new = Node()
        new.data = newData # 새로 입력 받을 값을 선언

        if self.front == None :#노드가 없다면
            self.front = new#새 노드가 front로 등록
            self.rear = new#새 노드가 rear로 등록

        else :
            self.rear.link = new#rear의 다음 노드에 등록
            self.rear = new#rear 등록

    def deQueue(self):
        if self.front == None:
            print("데이터가 없습니다.")

        else:
            delNode = self.front#첫 번째 노드를 삭제할 노드로 선언
            self.front = self.front.link
            #두번째 노드를 첫번째 노드로 front가 가리키도록 함
            if(self.front == None):
                #마지막 노드를 삭제하면 rear 또한 None으로 초기화
                self.rear = None
            del(delNode)#삭제

    

if __name__== "__main__":
    queue = LinkedQueue() # 함수 이용을 위한 객체 생성

    print('연결리스트를 이용한 Queue 프로그램입니다.\n')

    while True:
        print('\n1: 입력\t 2:삭제\t 3:출력\t 0:종료\n')
        
        ch = input("기능 선택--> ")
            
        if ch == '0': # 종료
            print('종료합니다\n')
            break

        elif ch == '1': # Queue 삽입
            newData = (input('입력할 자료: '))
            queue.enQueue(newData)
            queue.printQueue()

        elif ch == '2': # Queue 삭제
            queue.deQueue()
            queue.printQueue()

        elif ch ==  '3': # Queue 출력
            queue.printQueue()
            
        else:       
            print('\n잘못된 입력입니다.\n')

