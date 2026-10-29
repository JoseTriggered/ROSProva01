import rclpy
from rclpy.node import Node

from robo_interfaces.msg import Monitoramento


class RoboTopicoSubscriber(Node):
    
    def __init__(self):

        super().__init__('robo_topico_subscriber')

        self.subscription = self.create_subscription(
            Monitoramento, 'monitoramento', self.Callback, 10)

    def Callback(self, msg):

        seguro = 10.0 <= msg.temperatura <= 40.0 and msg.nivel_oxigenio > 80.0
        resultado = 'Safe' if seguro else 'Not Safe'

        self.get_logger().info(
            f'Oxigenio:{msg.nivel_oxigenio:.2f} | Temperatura:{msg.temperatura:.2f} | Estado: {resultado}')


def main(args=None):

    rclpy.init(args=args)
    node = RoboTopicoSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
