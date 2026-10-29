import random

import rclpy
from rclpy.node import Node

from robo_interfaces.srv import ColetaMaterial


class RoboColetaServidor(Node):

    def __init__(self):

        super().__init__('robo_coleta_servidor')
        
        self.srv = self.create_service(
            ColetaMaterial, 'coleta_material', self.Callback)
        
        self.get_logger().info('Servico coleta_material pronto.')

    def Callback(self, request, response):

        response.sucesso = random.randint(0, 7)

        self.get_logger().info(
            f'Requisicao: profundidade: {request.profundidade:.3f} -> sucesso: {response.sucesso}')
        
        return response


def main(args=None):

    rclpy.init(args=args)
    node = RoboColetaServidor()

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
