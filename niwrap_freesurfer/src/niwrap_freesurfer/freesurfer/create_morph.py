# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CREATE_MORPH_METADATA = Metadata(
    id="7ba94c2fde940591087049eddfc2da6806638f12.boutiques",
    name="createMorph",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


CreateMorphParameters = typing.TypedDict('CreateMorphParameters', {
    "__STYX_TYPE__": typing.Literal["createMorph"],
    "input_transforms": list[str],
    "output_transform": str,
    "template": typing.NotRequired[InputPathType | None],
    "subject": typing.NotRequired[InputPathType | None],
    "debug_coordinates": typing.NotRequired[list[float] | None],
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
        "createMorph": create_morph_cargs,
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
        "createMorph": create_morph_outputs,
    }.get(t)


class CreateMorphOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_morph(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform_file: OutputPathType
    """The resulting output transform file in tm3d format."""


def create_morph_params(
    input_transforms: list[str],
    output_transform: str,
    template: InputPathType | None = None,
    subject: InputPathType | None = None,
    debug_coordinates: list[float] | None = None,
) -> CreateMorphParameters:
    """
    Build parameters.
    
    Args:
        input_transforms: Input transforms, must specify type (affine, volume,\
            morph, mesh, gcam) with filename.
        output_transform: Output transform file in tm3d format.
        template: Template volume for geometry. Required if a gcam is present.
        subject: Subject volume for geometry.
        debug_coordinates: Coordinates for debugging purposes. Requires three\
            integer values.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "createMorph",
        "input_transforms": input_transforms,
        "output_transform": output_transform,
    }
    if template is not None:
        params["template"] = template
    if subject is not None:
        params["subject"] = subject
    if debug_coordinates is not None:
        params["debug_coordinates"] = debug_coordinates
    return params


def create_morph_cargs(
    params: CreateMorphParameters,
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
    cargs.append("createMorph")
    cargs.extend([
        "--in",
        *params.get("input_transforms")
    ])
    cargs.extend([
        "--out",
        params.get("output_transform")
    ])
    if params.get("template") is not None:
        cargs.extend([
            "--template",
            execution.input_file(params.get("template"))
        ])
    if params.get("subject") is not None:
        cargs.extend([
            "--subject",
            execution.input_file(params.get("subject"))
        ])
    if params.get("debug_coordinates") is not None:
        cargs.extend([
            "--dbg",
            *map(str, params.get("debug_coordinates"))
        ])
    return cargs


def create_morph_outputs(
    params: CreateMorphParameters,
    execution: Execution,
) -> CreateMorphOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CreateMorphOutputs(
        root=execution.output_file("."),
        output_transform_file=execution.output_file(params.get("output_transform")),
    )
    return ret


def create_morph_execute(
    params: CreateMorphParameters,
    execution: Execution,
) -> CreateMorphOutputs:
    """
    Tool to create morphological transformations using specified input transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CreateMorphOutputs`).
    """
    params = execution.params(params)
    cargs = create_morph_cargs(params, execution)
    ret = create_morph_outputs(params, execution)
    execution.run(cargs)
    return ret


def create_morph(
    input_transforms: list[str],
    output_transform: str,
    template: InputPathType | None = None,
    subject: InputPathType | None = None,
    debug_coordinates: list[float] | None = None,
    runner: Runner | None = None,
) -> CreateMorphOutputs:
    """
    Tool to create morphological transformations using specified input transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_transforms: Input transforms, must specify type (affine, volume,\
            morph, mesh, gcam) with filename.
        output_transform: Output transform file in tm3d format.
        template: Template volume for geometry. Required if a gcam is present.
        subject: Subject volume for geometry.
        debug_coordinates: Coordinates for debugging purposes. Requires three\
            integer values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateMorphOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CREATE_MORPH_METADATA)
    params = create_morph_params(
        input_transforms=input_transforms,
        output_transform=output_transform,
        template=template,
        subject=subject,
        debug_coordinates=debug_coordinates,
    )
    return create_morph_execute(params, execution)


__all__ = [
    "CREATE_MORPH_METADATA",
    "CreateMorphOutputs",
    "CreateMorphParameters",
    "create_morph",
    "create_morph_params",
]
