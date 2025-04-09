# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_FIX_TOPOLOGY_METADATA = Metadata(
    id="64e2b9290f868ea668dfb0ff3a646a7a893619d6.boutiques",
    name="mris_fix_topology",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisFixTopologyParameters = typing.TypedDict('MrisFixTopologyParameters', {
    "__STYX_TYPE__": typing.Literal["mris_fix_topology"],
    "subject_name": str,
    "hemisphere": str,
    "orig_name": typing.NotRequired[str | None],
    "sphere_name": typing.NotRequired[str | None],
    "inflated_name": typing.NotRequired[str | None],
    "output_name": typing.NotRequired[str | None],
    "defect_base_name": typing.NotRequired[str | None],
    "write_fixed_inflated": bool,
    "verbose": bool,
    "verbose_low": bool,
    "warnings": bool,
    "errors": bool,
    "movies": bool,
    "intersect": bool,
    "mappings": bool,
    "correct_defect": typing.NotRequired[float | None],
    "niters": typing.NotRequired[float | None],
    "genetic": bool,
    "optimize": bool,
    "random": typing.NotRequired[float | None],
    "seed": typing.NotRequired[float | None],
    "diag": bool,
    "mgz": bool,
    "smooth": typing.NotRequired[float | None],
    "diagnostic_level": typing.NotRequired[float | None],
    "threads": typing.NotRequired[float | None],
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
        "mris_fix_topology": mris_fix_topology_cargs,
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


class MrisFixTopologyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_fix_topology(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_fix_topology_params(
    subject_name: str,
    hemisphere: str,
    orig_name: str | None = "orig.nofix",
    sphere_name: str | None = "qsphere.nofix",
    inflated_name: str | None = "inflated.nofix",
    output_name: str | None = "orig",
    defect_base_name: str | None = "defect",
    write_fixed_inflated: bool = False,
    verbose: bool = False,
    verbose_low: bool = False,
    warnings_: bool = False,
    errors: bool = False,
    movies: bool = False,
    intersect: bool = False,
    mappings: bool = False,
    correct_defect: float | None = None,
    niters: float | None = None,
    genetic: bool = False,
    optimize: bool = False,
    random_: float | None = None,
    seed: float | None = None,
    diag: bool = False,
    mgz: bool = False,
    smooth: float | None = None,
    diagnostic_level: float | None = None,
    threads: float | None = None,
) -> MrisFixTopologyParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name.
        hemisphere: Hemisphere.
        orig_name: Input orig name (default is orig.nofix).
        sphere_name: Sphere name (default is qsphere.nofix).
        inflated_name: Inflated name (default is inflated.nofix).
        output_name: Output name (default is orig).
        defect_base_name: Defect basename (default is defect).
        write_fixed_inflated: Write fixed inflated.
        verbose: Increase verbosity.
        verbose_low: Low verbosity.
        warnings_: Show warnings.
        errors: Show errors.
        movies: Generate movies.
        intersect: Check if the final surface self-intersects.
        mappings: Generate several different mappings.
        correct_defect: Correct specific defect number.
        niters: Number of iterations for genetic algorithm.
        genetic: Use genetic search.
        optimize: Optimize genetic search.
        random_: Use random search with specified iterations.
        seed: Set random number generator seed.
        diag: Sets DIAG_SAVE_DIAGS.
        mgz: Assume volumes are in mgz format.
        smooth: Smooth corrected surface by N iterations.
        diagnostic_level: Set diagnostic level.
        threads: Set number of OpenMP threads.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_fix_topology",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "write_fixed_inflated": write_fixed_inflated,
        "verbose": verbose,
        "verbose_low": verbose_low,
        "warnings": warnings_,
        "errors": errors,
        "movies": movies,
        "intersect": intersect,
        "mappings": mappings,
        "genetic": genetic,
        "optimize": optimize,
        "diag": diag,
        "mgz": mgz,
    }
    if orig_name is not None:
        params["orig_name"] = orig_name
    if sphere_name is not None:
        params["sphere_name"] = sphere_name
    if inflated_name is not None:
        params["inflated_name"] = inflated_name
    if output_name is not None:
        params["output_name"] = output_name
    if defect_base_name is not None:
        params["defect_base_name"] = defect_base_name
    if correct_defect is not None:
        params["correct_defect"] = correct_defect
    if niters is not None:
        params["niters"] = niters
    if random_ is not None:
        params["random"] = random_
    if seed is not None:
        params["seed"] = seed
    if smooth is not None:
        params["smooth"] = smooth
    if diagnostic_level is not None:
        params["diagnostic_level"] = diagnostic_level
    if threads is not None:
        params["threads"] = threads
    return params


def mris_fix_topology_cargs(
    params: MrisFixTopologyParameters,
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
    cargs.append("mris_fix_topology")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    if params.get("orig_name") is not None:
        cargs.extend([
            "-orig",
            params.get("orig_name")
        ])
    if params.get("sphere_name") is not None:
        cargs.extend([
            "-sphere",
            params.get("sphere_name")
        ])
    if params.get("inflated_name") is not None:
        cargs.extend([
            "-inflated",
            params.get("inflated_name")
        ])
    if params.get("output_name") is not None:
        cargs.extend([
            "-out",
            params.get("output_name")
        ])
    if params.get("defect_base_name") is not None:
        cargs.extend([
            "-defect",
            params.get("defect_base_name")
        ])
    if params.get("write_fixed_inflated"):
        cargs.append("-wi")
    if params.get("verbose"):
        cargs.append("-verbose")
    if params.get("verbose_low"):
        cargs.append("-verbose_low")
    if params.get("warnings"):
        cargs.append("-warnings")
    if params.get("errors"):
        cargs.append("-errors")
    if params.get("movies"):
        cargs.append("-movies")
    if params.get("intersect"):
        cargs.append("-intersect")
    if params.get("mappings"):
        cargs.append("-mappings")
    if params.get("correct_defect") is not None:
        cargs.extend([
            "-correct_defect",
            str(params.get("correct_defect"))
        ])
    if params.get("niters") is not None:
        cargs.extend([
            "-niters",
            str(params.get("niters"))
        ])
    if params.get("genetic"):
        cargs.append("-genetic")
    if params.get("optimize"):
        cargs.append("-optimize")
    if params.get("random") is not None:
        cargs.extend([
            "-random",
            str(params.get("random"))
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "-seed",
            str(params.get("seed"))
        ])
    if params.get("diag"):
        cargs.append("-diag")
    if params.get("mgz"):
        cargs.append("-mgz")
    if params.get("smooth") is not None:
        cargs.extend([
            "-s",
            str(params.get("smooth"))
        ])
    if params.get("diagnostic_level") is not None:
        cargs.extend([
            "-v",
            str(params.get("diagnostic_level"))
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "-threads",
            str(params.get("threads"))
        ])
    return cargs


def mris_fix_topology_outputs(
    params: MrisFixTopologyParameters,
    execution: Execution,
) -> MrisFixTopologyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisFixTopologyOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_fix_topology_execute(
    params: MrisFixTopologyParameters,
    execution: Execution,
) -> MrisFixTopologyOutputs:
    """
    Computes a mapping from the unit sphere onto the cortical surface, ensuring a
    topologically correct surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisFixTopologyOutputs`).
    """
    params = execution.params(params)
    cargs = mris_fix_topology_cargs(params, execution)
    ret = mris_fix_topology_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_fix_topology(
    subject_name: str,
    hemisphere: str,
    orig_name: str | None = "orig.nofix",
    sphere_name: str | None = "qsphere.nofix",
    inflated_name: str | None = "inflated.nofix",
    output_name: str | None = "orig",
    defect_base_name: str | None = "defect",
    write_fixed_inflated: bool = False,
    verbose: bool = False,
    verbose_low: bool = False,
    warnings_: bool = False,
    errors: bool = False,
    movies: bool = False,
    intersect: bool = False,
    mappings: bool = False,
    correct_defect: float | None = None,
    niters: float | None = None,
    genetic: bool = False,
    optimize: bool = False,
    random_: float | None = None,
    seed: float | None = None,
    diag: bool = False,
    mgz: bool = False,
    smooth: float | None = None,
    diagnostic_level: float | None = None,
    threads: float | None = None,
    runner: Runner | None = None,
) -> MrisFixTopologyOutputs:
    """
    Computes a mapping from the unit sphere onto the cortical surface, ensuring a
    topologically correct surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name.
        hemisphere: Hemisphere.
        orig_name: Input orig name (default is orig.nofix).
        sphere_name: Sphere name (default is qsphere.nofix).
        inflated_name: Inflated name (default is inflated.nofix).
        output_name: Output name (default is orig).
        defect_base_name: Defect basename (default is defect).
        write_fixed_inflated: Write fixed inflated.
        verbose: Increase verbosity.
        verbose_low: Low verbosity.
        warnings_: Show warnings.
        errors: Show errors.
        movies: Generate movies.
        intersect: Check if the final surface self-intersects.
        mappings: Generate several different mappings.
        correct_defect: Correct specific defect number.
        niters: Number of iterations for genetic algorithm.
        genetic: Use genetic search.
        optimize: Optimize genetic search.
        random_: Use random search with specified iterations.
        seed: Set random number generator seed.
        diag: Sets DIAG_SAVE_DIAGS.
        mgz: Assume volumes are in mgz format.
        smooth: Smooth corrected surface by N iterations.
        diagnostic_level: Set diagnostic level.
        threads: Set number of OpenMP threads.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisFixTopologyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_FIX_TOPOLOGY_METADATA)
    params = mris_fix_topology_params(
        subject_name=subject_name,
        hemisphere=hemisphere,
        orig_name=orig_name,
        sphere_name=sphere_name,
        inflated_name=inflated_name,
        output_name=output_name,
        defect_base_name=defect_base_name,
        write_fixed_inflated=write_fixed_inflated,
        verbose=verbose,
        verbose_low=verbose_low,
        warnings_=warnings_,
        errors=errors,
        movies=movies,
        intersect=intersect,
        mappings=mappings,
        correct_defect=correct_defect,
        niters=niters,
        genetic=genetic,
        optimize=optimize,
        random_=random_,
        seed=seed,
        diag=diag,
        mgz=mgz,
        smooth=smooth,
        diagnostic_level=diagnostic_level,
        threads=threads,
    )
    return mris_fix_topology_execute(params, execution)


__all__ = [
    "MRIS_FIX_TOPOLOGY_METADATA",
    "MrisFixTopologyOutputs",
    "MrisFixTopologyParameters",
    "mris_fix_topology",
    "mris_fix_topology_params",
]
