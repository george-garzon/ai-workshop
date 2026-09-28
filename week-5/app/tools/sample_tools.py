from app.models.tools import (
    LookupAccountArgs,
    SearchKnowledgeBaseArgs,
    SendMessageArgs,
)


async def search_knowledge_base(args: SearchKnowledgeBaseArgs):
    raise NotImplementedError("Implement knowledge-base search.")


async def lookup_account(args: LookupAccountArgs):
    raise NotImplementedError("Implement account lookup.")


async def send_message(args: SendMessageArgs):
    raise NotImplementedError("Implement sensitive message sending.")
