# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_FIRST_METADATA = Metadata(
    id="dfdd3ac896156c070344b1fbb233ffd1dc97ea8d.boutiques",
    name="run_first",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


RunFirstParameters = typing.TypedDict('RunFirstParameters', {
    "__STYXTYPE__": typing.Literal["run_first"],
    "input_image": InputPathType,
    "transformation_matrix": InputPathType,
    "n_modes": float,
    "output_basename": str,
    "model_name": InputPathType,
    "verbose_flag": bool,
    "intref_model_name": typing.NotRequired[str | None],
    "load_bvars": typing.NotRequired[InputPathType | None],
    "multiple_images_flag": bool,
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
        "run_first": run_first_cargs,
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
        "run_first": run_first_outputs,
    }.get(t)


class RunFirstOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_first(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated by FIRST"""


def run_first_params(
    input_image: InputPathType,
    transformation_matrix: InputPathType,
    n_modes: float,
    output_basename: str,
    model_name: InputPathType,
    verbose_flag: bool = False,
    intref_model_name: str | None = None,
    load_bvars: InputPathType | None = None,
    multiple_images_flag: bool = False,
) -> RunFirstParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image file (e.g. img.nii.gz).
        transformation_matrix: Input transformation matrix file (e.g.\
            input_to_mni.mat).
        n_modes: Number of modes.
        output_basename: Output basename.
        model_name: Model name.
        verbose_flag: Verbose mode.
        intref_model_name: Reference structure for the local intensity\
            normalization.
        load_bvars: Initializes FIRST with a previous estimate of the structure.
        multiple_images_flag: Run FIRST on multiple images; provide a list of\
            images, transformation matrices, and output names.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_first",
        "input_image": input_image,
        "transformation_matrix": transformation_matrix,
        "n_modes": n_modes,
        "output_basename": output_basename,
        "model_name": model_name,
        "verbose_flag": verbose_flag,
        "multiple_images_flag": multiple_images_flag,
    }
    if intref_model_name is not None:
        params["intref_model_name"] = intref_model_name
    if load_bvars is not None:
        params["load_bvars"] = load_bvars
    return params


def run_first_cargs(
    params: RunFirstParameters,
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
    cargs.append("run_first")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    cargs.extend([
        "-t",
        execution.input_file(params.get("transformation_matrix"))
    ])
    cargs.extend([
        "-n",
        str(params.get("n_modes"))
    ])
    cargs.extend([
        "-o",
        params.get("output_basename")
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("model_name"))
    ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("intref_model_name") is not None:
        cargs.extend([
            "-intref",
            params.get("intref_model_name")
        ])
    if params.get("load_bvars") is not None:
        cargs.extend([
            "-loadBvars",
            execution.input_file(params.get("load_bvars"))
        ])
    if params.get("multiple_images_flag"):
        cargs.append("-multipleImages")
    return cargs


def run_first_outputs(
    params: RunFirstParameters,
    execution: Execution,
) -> RunFirstOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunFirstOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("output_basename") + "*"),
    )
    return ret


def run_first_execute(
    params: RunFirstParameters,
    execution: Execution,
) -> RunFirstOutputs:
    """
    A tool to run FSL's FIRST for subcortical segmentation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunFirstOutputs`).
    """
    params = execution.params(params)
    cargs = run_first_cargs(params, execution)
    ret = run_first_outputs(params, execution)
    execution.run(cargs)
    return ret


def run_first(
    input_image: InputPathType,
    transformation_matrix: InputPathType,
    n_modes: float,
    output_basename: str,
    model_name: InputPathType,
    verbose_flag: bool = False,
    intref_model_name: str | None = None,
    load_bvars: InputPathType | None = None,
    multiple_images_flag: bool = False,
    runner: Runner | None = None,
) -> RunFirstOutputs:
    """
    A tool to run FSL's FIRST for subcortical segmentation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image file (e.g. img.nii.gz).
        transformation_matrix: Input transformation matrix file (e.g.\
            input_to_mni.mat).
        n_modes: Number of modes.
        output_basename: Output basename.
        model_name: Model name.
        verbose_flag: Verbose mode.
        intref_model_name: Reference structure for the local intensity\
            normalization.
        load_bvars: Initializes FIRST with a previous estimate of the structure.
        multiple_images_flag: Run FIRST on multiple images; provide a list of\
            images, transformation matrices, and output names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunFirstOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_FIRST_METADATA)
    params = run_first_params(
        input_image=input_image,
        transformation_matrix=transformation_matrix,
        n_modes=n_modes,
        output_basename=output_basename,
        model_name=model_name,
        verbose_flag=verbose_flag,
        intref_model_name=intref_model_name,
        load_bvars=load_bvars,
        multiple_images_flag=multiple_images_flag,
    )
    return run_first_execute(params, execution)


__all__ = [
    "RUN_FIRST_METADATA",
    "RunFirstOutputs",
    "RunFirstParameters",
    "run_first",
    "run_first_params",
]
