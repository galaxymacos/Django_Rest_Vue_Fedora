from rest_framework.decorators import api_view
from rest_framework.response import Response

from vehicles.models import Tool
from vehicles.serializers.tools import ToolSerializer


@api_view(["GET"])
def list_tools(request):
    tools = [
        Tool("hammer", "Mastercraft"),
        Tool("wrench", "Husky"),
    ]
    tool = Tool("screwdriver", "Stanley")
    tools.append(tool)

    serializer = ToolSerializer(tools, many=True)
    content = {"tools": serializer.data}
    return Response(content)
