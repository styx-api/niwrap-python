# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SCENE_FILE_MERGE_METADATA = Metadata(
    id="166825a4f2488129798817b6bae35677b4bafe8f.boutiques",
    name="scene-file-merge",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SceneFileMergeUpToParameters = typing.TypedDict('SceneFileMergeUpToParameters', {
    "__STYXTYPE__": typing.Literal["up_to"],
    "last_column": str,
    "opt_reverse": bool,
})


SceneFileMergeSceneParameters = typing.TypedDict('SceneFileMergeSceneParameters', {
    "__STYXTYPE__": typing.Literal["scene"],
    "scene": str,
    "up_to": typing.NotRequired[SceneFileMergeUpToParameters | None],
})


SceneFileMergeSceneFileParameters = typing.TypedDict('SceneFileMergeSceneFileParameters', {
    "__STYXTYPE__": typing.Literal["scene_file"],
    "scene_file": str,
    "scene": typing.NotRequired[list[SceneFileMergeSceneParameters] | None],
})


SceneFileMergeParameters = typing.TypedDict('SceneFileMergeParameters', {
    "__STYXTYPE__": typing.Literal["scene-file-merge"],
    "scene_file_out": str,
    "scene_file": typing.NotRequired[list[SceneFileMergeSceneFileParameters] | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "scene-file-merge": scene_file_merge_cargs,
        "scene_file": scene_file_merge_scene_file_cargs,
        "scene": scene_file_merge_scene_cargs,
        "up_to": scene_file_merge_up_to_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


def scene_file_merge_up_to_params(
    last_column: str,
    opt_reverse: bool = False,
) -> SceneFileMergeUpToParameters:
    """
    Build parameters.
    
    Args:
        last_column: the number or name of the last scene to include.
        opt_reverse: use the range in reverse order.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "up_to",
        "last_column": last_column,
        "opt_reverse": opt_reverse,
    }
    return params


def scene_file_merge_up_to_cargs(
    params: SceneFileMergeUpToParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-up-to")
    cargs.append(params.get("last_column"))
    if params.get("opt_reverse"):
        cargs.append("-reverse")
    return cargs


def scene_file_merge_scene_params(
    scene: str,
    up_to: SceneFileMergeUpToParameters | None = None,
) -> SceneFileMergeSceneParameters:
    """
    Build parameters.
    
    Args:
        scene: the scene number or name.
        up_to: use an inclusive range of scenes.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "scene",
        "scene": scene,
    }
    if up_to is not None:
        params["up_to"] = up_to
    return params


def scene_file_merge_scene_cargs(
    params: SceneFileMergeSceneParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-scene")
    cargs.append(params.get("scene"))
    if params.get("up_to") is not None:
        cargs.extend(dyn_cargs(params.get("up_to")["__STYXTYPE__"])(params.get("up_to"), execution))
    return cargs


def scene_file_merge_scene_file_params(
    scene_file: str,
    scene: list[SceneFileMergeSceneParameters] | None = None,
) -> SceneFileMergeSceneFileParameters:
    """
    Build parameters.
    
    Args:
        scene_file: the input scene file.
        scene: specify a scene to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "scene_file",
        "scene_file": scene_file,
    }
    if scene is not None:
        params["scene"] = scene
    return params


def scene_file_merge_scene_file_cargs(
    params: SceneFileMergeSceneFileParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-scene-file")
    cargs.append(params.get("scene_file"))
    if params.get("scene") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("scene")] for a in c])
    return cargs


class SceneFileMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_merge_params(
    scene_file_out: str,
    scene_file: list[SceneFileMergeSceneFileParameters] | None = None,
) -> SceneFileMergeParameters:
    """
    Build parameters.
    
    Args:
        scene_file_out: output - the output scene file.
        scene_file: specify a scene file to use scenes from.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "scene-file-merge",
        "scene_file_out": scene_file_out,
    }
    if scene_file is not None:
        params["scene_file"] = scene_file
    return params


def scene_file_merge_cargs(
    params: SceneFileMergeParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-file-merge")
    cargs.append(params.get("scene_file_out"))
    if params.get("scene_file") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("scene_file")] for a in c])
    return cargs


def scene_file_merge_outputs(
    params: SceneFileMergeParameters,
    execution: Execution,
) -> SceneFileMergeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SceneFileMergeOutputs(
        root=execution.output_file("."),
    )
    return ret


def scene_file_merge_execute(
    params: SceneFileMergeParameters,
    execution: Execution,
) -> SceneFileMergeOutputs:
    """
    Rearrange scenes into a new file.
    
    Takes one or more scene files and constructs a new scene file by
    concatenating specified scenes from them.
    
    Example: wb_command -scene-file-merge out.scene -scene-file first.scene
    -scene 1 -scene-file second.scene
    
    This example would take the first scene from first.scene, followed by all
    scenes from second.scene, and write these scenes to out.scene.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SceneFileMergeOutputs`).
    """
    params = execution.params(params)
    cargs = scene_file_merge_cargs(params, execution)
    ret = scene_file_merge_outputs(params, execution)
    execution.run(cargs)
    return ret


def scene_file_merge(
    scene_file_out: str,
    scene_file: list[SceneFileMergeSceneFileParameters] | None = None,
    runner: Runner | None = None,
) -> SceneFileMergeOutputs:
    """
    Rearrange scenes into a new file.
    
    Takes one or more scene files and constructs a new scene file by
    concatenating specified scenes from them.
    
    Example: wb_command -scene-file-merge out.scene -scene-file first.scene
    -scene 1 -scene-file second.scene
    
    This example would take the first scene from first.scene, followed by all
    scenes from second.scene, and write these scenes to out.scene.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        scene_file_out: output - the output scene file.
        scene_file: specify a scene file to use scenes from.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SceneFileMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCENE_FILE_MERGE_METADATA)
    params = scene_file_merge_params(
        scene_file_out=scene_file_out,
        scene_file=scene_file,
    )
    return scene_file_merge_execute(params, execution)


__all__ = [
    "SCENE_FILE_MERGE_METADATA",
    "SceneFileMergeOutputs",
    "SceneFileMergeParameters",
    "SceneFileMergeSceneFileParameters",
    "SceneFileMergeSceneParameters",
    "SceneFileMergeUpToParameters",
    "scene_file_merge",
    "scene_file_merge_params",
    "scene_file_merge_scene_file_params",
    "scene_file_merge_scene_params",
    "scene_file_merge_up_to_params",
]
