# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONVERT_AFFINE_METADATA = Metadata(
    id="3b8860ef222f898c6a65c82c6ffa70dc64abc45b.boutiques",
    name="convert-affine",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


ConvertAffineFromWorldParameters = typing.TypedDict('ConvertAffineFromWorldParameters', {
    "__STYX_TYPE__": typing.Literal["from_world"],
    "input": str,
    "opt_inverse": bool,
})


ConvertAffineFromFlirtParameters = typing.TypedDict('ConvertAffineFromFlirtParameters', {
    "__STYX_TYPE__": typing.Literal["from_flirt"],
    "input": str,
    "source_volume": str,
    "target_volume": str,
})


ConvertAffineToWorldParameters = typing.TypedDict('ConvertAffineToWorldParameters', {
    "__STYX_TYPE__": typing.Literal["to_world"],
    "output": str,
    "opt_inverse": bool,
})


ConvertAffineToFlirtParameters = typing.TypedDict('ConvertAffineToFlirtParameters', {
    "__STYX_TYPE__": typing.Literal["to_flirt"],
    "output": str,
    "source_volume": str,
    "target_volume": str,
})


ConvertAffineParameters = typing.TypedDict('ConvertAffineParameters', {
    "__STYX_TYPE__": typing.Literal["convert-affine"],
    "from_world": typing.NotRequired[ConvertAffineFromWorldParameters | None],
    "opt_from_itk_input": typing.NotRequired[str | None],
    "from_flirt": typing.NotRequired[ConvertAffineFromFlirtParameters | None],
    "to_world": typing.NotRequired[ConvertAffineToWorldParameters | None],
    "opt_to_itk_output": typing.NotRequired[str | None],
    "to_flirt": typing.NotRequired[list[ConvertAffineToFlirtParameters] | None],
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
        "convert-affine": convert_affine_cargs,
        "from_world": convert_affine_from_world_cargs,
        "from_flirt": convert_affine_from_flirt_cargs,
        "to_world": convert_affine_to_world_cargs,
        "to_flirt": convert_affine_to_flirt_cargs,
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


def convert_affine_from_world_params(
    input_: str,
    opt_inverse: bool = False,
) -> ConvertAffineFromWorldParameters:
    """
    Build parameters.
    
    Args:
        input_: the input affine.
        opt_inverse: for files that use 'target to source' convention.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "from_world",
        "input": input_,
        "opt_inverse": opt_inverse,
    }
    return params


def convert_affine_from_world_cargs(
    params: ConvertAffineFromWorldParameters,
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
    cargs.append("-from-world")
    cargs.append(params.get("input"))
    if params.get("opt_inverse"):
        cargs.append("-inverse")
    return cargs


def convert_affine_from_flirt_params(
    input_: str,
    source_volume: str,
    target_volume: str,
) -> ConvertAffineFromFlirtParameters:
    """
    Build parameters.
    
    Args:
        input_: the input affine.
        source_volume: the source volume used when generating the input affine.
        target_volume: the target volume used when generating the input affine.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "from_flirt",
        "input": input_,
        "source_volume": source_volume,
        "target_volume": target_volume,
    }
    return params


def convert_affine_from_flirt_cargs(
    params: ConvertAffineFromFlirtParameters,
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
    cargs.append("-from-flirt")
    cargs.append(params.get("input"))
    cargs.append(params.get("source_volume"))
    cargs.append(params.get("target_volume"))
    return cargs


def convert_affine_to_world_params(
    output: str,
    opt_inverse: bool = False,
) -> ConvertAffineToWorldParameters:
    """
    Build parameters.
    
    Args:
        output: output - the output affine.
        opt_inverse: write file using 'target to source' convention.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "to_world",
        "output": output,
        "opt_inverse": opt_inverse,
    }
    return params


def convert_affine_to_world_cargs(
    params: ConvertAffineToWorldParameters,
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
    cargs.append("-to-world")
    cargs.append(params.get("output"))
    if params.get("opt_inverse"):
        cargs.append("-inverse")
    return cargs


def convert_affine_to_flirt_params(
    output: str,
    source_volume: str,
    target_volume: str,
) -> ConvertAffineToFlirtParameters:
    """
    Build parameters.
    
    Args:
        output: output - the output affine.
        source_volume: the volume you want to apply the transform to.
        target_volume: the target space you want the transformed volume to\
            match.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "to_flirt",
        "output": output,
        "source_volume": source_volume,
        "target_volume": target_volume,
    }
    return params


def convert_affine_to_flirt_cargs(
    params: ConvertAffineToFlirtParameters,
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
    cargs.append("-to-flirt")
    cargs.append(params.get("output"))
    cargs.append(params.get("source_volume"))
    cargs.append(params.get("target_volume"))
    return cargs


class ConvertAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_affine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def convert_affine_params(
    from_world: ConvertAffineFromWorldParameters | None = None,
    opt_from_itk_input: str | None = None,
    from_flirt: ConvertAffineFromFlirtParameters | None = None,
    to_world: ConvertAffineToWorldParameters | None = None,
    opt_to_itk_output: str | None = None,
    to_flirt: list[ConvertAffineToFlirtParameters] | None = None,
) -> ConvertAffineParameters:
    """
    Build parameters.
    
    Args:
        from_world: input is a NIFTI 'world' affine.
        opt_from_itk_input: input is an ITK matrix: the input affine.
        from_flirt: input is a flirt matrix.
        to_world: write output as a NIFTI 'world' affine.
        opt_to_itk_output: write output as an ITK affine: output - the output\
            affine.
        to_flirt: write output as a flirt matrix.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convert-affine",
    }
    if from_world is not None:
        params["from_world"] = from_world
    if opt_from_itk_input is not None:
        params["opt_from_itk_input"] = opt_from_itk_input
    if from_flirt is not None:
        params["from_flirt"] = from_flirt
    if to_world is not None:
        params["to_world"] = to_world
    if opt_to_itk_output is not None:
        params["opt_to_itk_output"] = opt_to_itk_output
    if to_flirt is not None:
        params["to_flirt"] = to_flirt
    return params


def convert_affine_cargs(
    params: ConvertAffineParameters,
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
    cargs.append("-convert-affine")
    if params.get("from_world") is not None:
        cargs.extend(dyn_cargs(params.get("from_world")["__STYXTYPE__"])(params.get("from_world"), execution))
    if params.get("opt_from_itk_input") is not None:
        cargs.extend([
            "-from-itk",
            params.get("opt_from_itk_input")
        ])
    if params.get("from_flirt") is not None:
        cargs.extend(dyn_cargs(params.get("from_flirt")["__STYXTYPE__"])(params.get("from_flirt"), execution))
    if params.get("to_world") is not None:
        cargs.extend(dyn_cargs(params.get("to_world")["__STYXTYPE__"])(params.get("to_world"), execution))
    if params.get("opt_to_itk_output") is not None:
        cargs.extend([
            "-to-itk",
            params.get("opt_to_itk_output")
        ])
    if params.get("to_flirt") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("to_flirt")] for a in c])
    return cargs


def convert_affine_outputs(
    params: ConvertAffineParameters,
    execution: Execution,
) -> ConvertAffineOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertAffineOutputs(
        root=execution.output_file("."),
    )
    return ret


def convert_affine_execute(
    params: ConvertAffineParameters,
    execution: Execution,
) -> ConvertAffineOutputs:
    """
    Convert an affine file between conventions.
    
    NIFTI world matrices can be used directly on mm coordinates via matrix
    multiplication, they use the NIFTI coordinate system, that is, positive X is
    right, positive Y is anterior, and positive Z is superior. Note that
    wb_command assumes that world matrices transform source coordinates to
    target coordinates, while other tools may use affines that transform target
    coordinates to source coordinates.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-flirt may be specified more than once.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertAffineOutputs`).
    """
    params = execution.params(params)
    cargs = convert_affine_cargs(params, execution)
    ret = convert_affine_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_affine(
    from_world: ConvertAffineFromWorldParameters | None = None,
    opt_from_itk_input: str | None = None,
    from_flirt: ConvertAffineFromFlirtParameters | None = None,
    to_world: ConvertAffineToWorldParameters | None = None,
    opt_to_itk_output: str | None = None,
    to_flirt: list[ConvertAffineToFlirtParameters] | None = None,
    runner: Runner | None = None,
) -> ConvertAffineOutputs:
    """
    Convert an affine file between conventions.
    
    NIFTI world matrices can be used directly on mm coordinates via matrix
    multiplication, they use the NIFTI coordinate system, that is, positive X is
    right, positive Y is anterior, and positive Z is superior. Note that
    wb_command assumes that world matrices transform source coordinates to
    target coordinates, while other tools may use affines that transform target
    coordinates to source coordinates.
    
    The ITK format is used by ANTS.
    
    You must specify exactly one -from option, but you may specify multiple -to
    options, and -to-flirt may be specified more than once.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        from_world: input is a NIFTI 'world' affine.
        opt_from_itk_input: input is an ITK matrix: the input affine.
        from_flirt: input is a flirt matrix.
        to_world: write output as a NIFTI 'world' affine.
        opt_to_itk_output: write output as an ITK affine: output - the output\
            affine.
        to_flirt: write output as a flirt matrix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertAffineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_AFFINE_METADATA)
    params = convert_affine_params(
        from_world=from_world,
        opt_from_itk_input=opt_from_itk_input,
        from_flirt=from_flirt,
        to_world=to_world,
        opt_to_itk_output=opt_to_itk_output,
        to_flirt=to_flirt,
    )
    return convert_affine_execute(params, execution)


__all__ = [
    "CONVERT_AFFINE_METADATA",
    "ConvertAffineFromFlirtParameters",
    "ConvertAffineFromWorldParameters",
    "ConvertAffineOutputs",
    "ConvertAffineParameters",
    "ConvertAffineToFlirtParameters",
    "ConvertAffineToWorldParameters",
    "convert_affine",
    "convert_affine_from_flirt_params",
    "convert_affine_from_world_params",
    "convert_affine_params",
    "convert_affine_to_flirt_params",
    "convert_affine_to_world_params",
]
